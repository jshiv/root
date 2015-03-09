# root

root is a template folder structure for organizing workflows 

###Folders structure
  - repos
  - projects
  - plaground


repos is dedicated to maintaining source code and reposotories such as this one. 
>The folder includes sample python package which can be used as a template for developing your own packages. This repo can be setup from the command line via:
```
cd ~
git clone https://github.com/jshiv/root.git
cd root
```
>and they python package can be installed via:
```
cd repos
python setup.py install
```

###projects

projects contains a standard setup for project orginization.

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
