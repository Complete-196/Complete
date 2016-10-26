# Complete
## This app is awesome !!!
#### @authors tiopi, aokennard
The front end will be done in HTML, Sass and Angular.JS

The backend will be done in python using django or flask


##Mac
To use this project, you have to download pip and a virtualenv.
For pip:
```
$ sudo easy_install pip
```
For the virtualenv:
```
$ pip install virtualenv virtualenvwrapper
```

Once the virtualenv is installed, Django is required for the project:
To enter virtual environment
```
$ source venv/bin/activate
$ pip install django
```

The setup for the project is finished. Specification of the interpreter is required, use virtualenv python 2.7.


##Windows 8
To use the project, you need to have pip and a virtual environment installed.
For installing pip (assuming python doesn't have it bundled):
Download get-pip.py : https://bootstrap.pypa.io/get-pip.py, save it as a .py file
Run in command prompt/powershell:
```
$ python get-pip.py
```
For installing the virtual environment:
```
$ pip install virtualenv
$ pip install virtualenvwrapper-powershell
```
Next, run Windows Powershell as an Administrator 
(generally found in C:\Windows\System32\WindowsPowerShell\v1.0C:\Windows\System32\WindowsPowerShell\v1.0)
Once in, you need to change your script execution policy:
```
$ Set-ExecutionPolicy RemoteSigned
```
Choose yes, then next change directory to where you want to have your virtualenv folder.
Once you you are in the directory, create a virtualenv folder:
```
$ virtualenv .\<virtual-env-name-here>
```
To start your virtual environment:
```
$ .\<virtual-env-name-here>\Scripts\activate
```
Once in the virtual environment, denoted by a prefix of (virtual-env-name-here) in your shell, you need to install django:
```
$ pip install django
```
The setup for the project is finished. Specification of the interpreter is required, use virtualenv python 2.7.
