from template import utils as ut
'''
Creates a folder directory consisting of a root folder named [date]_[project] 
(date optional), and subfolders input and results, as well as copies a requirements.txt file 
(optional). Run this by typing '$python makeDir.py'.
'''

#ask for user input on project details
name = raw_input("Please enter name of project: ")
date = raw_input("Do you want to timestamp the folder name?: ")

if date.lower()[0] == 'y':
    date = True
else:
    date = False

#run function
ut.makeProjectDir(name, date = date, root = './' )