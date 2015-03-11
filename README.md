# root

root is a template folder structure for organizing work-flows 

###Folders structure
  - repos
  - projects
  - playground
  - docs


###repos

repos is dedicated to maintaining source code and repositories. 
>The folder includes sample python package which can be used as a template for developing your own packages. Go ahead and download this folder structure as a zip on the right hand side of the git hub page.

>The python package can be installed via:
```
cd root-master
cd repos
cd template
python setup.py install
```

###projects

projects contains a standard setup for project organization.

>The folder structure is as follows:

    projects
        mkdir.py "file for generating new project folders"
        template
            ipynbs "development notebooks"
            scripts "project scripts"
            input "input data"
            results "output data"
                csv
                figures 
                pickle
                json
            requirements.txt "pip install -f requirements.txt"
>running the mkdir.py will generate a new folder with the the same structure as the template folder
```
python mkdir.py
```

###playground
playground maintains the primary development environment 

>The folder structure of playground is designed to organize development efforts into typical design patterns, split between explicit package development to loose experimentation. 

    playground
        dev "package development"
            data
            input
            results
        scratch "loose experimentation"
        

###docs
docs maintains a folder structure for general documentation and setup shell scripts

    docs
      whitepapers 
      notes
      setup

**Note**
> This repo is meant to serve as a work-flow template and not as a repository in and of its self. It is best to back up your work in the cloud and use github for the folders inside the repos folder.
