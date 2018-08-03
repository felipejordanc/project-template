# project-template

This is a very simple template to initialize a research project. You can run the init.py script on your machine and the following useful directories will be created:

* A remote folder: This is not actually remote, in the sence that lives in the same machine, but is a symbolic link to a folder in your machine that has the project for the data. Usually that folder lives in Dropbox or Google Drive. **This folder is ignored by git**, keeping the heavy stuff out of git but allowing you to have the same file structure than your colaborators.

* A local folder: Here you can put scripts for experimentation that you are not ready to share. It may be also usefull to save data that you don't want to have into you remote folder, but in taht case the files/paths should be created programatically for the code to work for everyone. **This folder is ignored by git***.

* A scripts folder: Here you put the code you share with your colaborators. **This folder is tracked by git**.

* A tex folder: Here you put the latex files of your paper. **This folder is tracked by git**.

The .gitignore that comes with this project ignores the usual python and latex stuff (picked up from elsewere, credited in the file).

Comments are welcome!
