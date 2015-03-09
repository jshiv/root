import os
import sys
import datetime as dt
import shutil



def create_dir(path, dirDict = {}):

    '''
    Tries to create a new directory in the given path. 
    **create_dir** can also create subfolders according to the dictionnary given as second argument.

    Parameters
    ----------
    path : string 
        string giving the path of the location to create the directory, either absolute or relative.
    dirDict : dictionnary, optional (the default is {}, which means that no subfolders will be created)
        Dictionnary ordering the creation of subfolders. Keys must be strings, and values either None or path dictionnaries.

    Examples
    --------

    >>> path = './project'
    >>> dirDict = {'dir1':None, 'dir2':{'subdir21':None}}
    >>> utils.create_dir(path,dirDict)

    will create:

    * *project/dir1* 
    * *project/dir2/subdir21* 

    in your parent directory.

    '''

    folders = path.split('/')
    folders = [i for i in folders if i != '']
    rootPath = ''
    if folders[0] == 'C:':
        folders = folders[1:]
    count = 0
    for directory in folders:
        count += 1
        
        if (directory[0] == '.') & (count == 1):#required to handle the dot operators 
            rootPath = directory 
        else:
            rootPath = rootPath + '/' + directory
        try:
            os.makedirs(rootPath)
        #If the file already exists (EEXIST), raise exception and do nothing
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    for key in dirDict.keys():
        rootPath = path + "/" + key
        try:
            os.makedirs(rootPath)
        #If the file already exists (EEXIST), raise exception and do nothing
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        if dirDict[key] is not None:
            create_dir(rootPath, dirDict[key])


def makeProjectDir(name, date = True, copyDir = './template', root = './' ):

    '''
    Takes name of project and date boolean to create a standard project folder.
    Writes to root, or root path provided.
    Copies directory of stuff from copyDir to folder.

    Parameters
    ----------
    name : string
        Name of the project 
    date : bool (default is *True*)
        If *True*, includes the creation date in the name of the project main directory
    copyDir : string (default is *'./template'*)
        Path of a directory to copy inside the project directory
    root : string (default is *'./'*, which means the directory is created in the local root)
        Desired location path for the project directory. Can be absolute or relative.

    Notes
    -----
    The project directory created includes 5 folders: *csv*, *figures*, *json*, *pickle*, *html*, 
    as well as a *readme.txt* file providing the author of the directory (in Linux os) as well as the creation date.

    '''

    #create folder name w/optional date
    if date == False:
        folder_name = name.replace(' ', '_')
    else:
        date = dt.datetime.now().strftime('%m%d%y')
        folder_name = date+'_'+name.replace(' ', '_')
    print folder_name

    #format root name
    root = root+(1-root.endswith('/'))*'/'

    #if given a copyDir full of requirements.txt, .gitignores, etc., copy it over
    try:
        shutil.copytree(copyDir, root+folder_name)
        print 'copied copyDir on over'
    except:
        print 'failed at copying copyDir folder'

    #create the root directory under [root]/[date]_[name]
        try:
            create_dir(root+folder_name, dirDict = {'input':None, 
                                                    'results':dict(csv = None, figures = None, json = None, pickle = None, html=None)})
        except:
            print 'error. creating of folders failed. possible duplicate'
                
    #create readme.txt file
    if sys.platform.find('linux')!=-1:
        readthis = 'created by: '+os.getlogin()+'\ncreated at: '+str(dt.datetime.now())
    else:
        readthis = 'created at: '+str(dt.datetime.now())

    fd = os.open(root+folder_name+"/readme.txt", os.O_RDWR|os.O_CREAT)
    os.write(fd, readthis); os.close(fd)
    print 'bam, done.'