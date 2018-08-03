
import os, sys, re, time

if os.path.exists('remote') or os.path.exists('local') or os.path.exists('scripts') or os.path.exists('tex'):
    sys.exit('This project has already been initialized.')

print('\n')

print('This script will initialize a research project at {0}. It will create the following folders:\n'.format(os.getcwd()))

print("- A remote folder, which is a symbolic link to a folder where you store the data for this project, ussually located in your Dropbox or Google Drive. This folder will be ignored by git.\n")

print("- A local folder where you can place scripts used for experimentation. You can also use this folder to locally store data that you don't want to have in your remote data folder, although in that case you should programatically create the necessary subdirectories and files if you want your colaborators to be able to reproduce your results with the shared code. This folder will be ignored by git.\n")

print("- A script folder where you can put the scripts you share with your colaborators. This folder will be tracked by git.\n")

print("- A tex folder where you can put the tex files you share with your colaborators. This folder will be tracked by git.\n")

print("You can costumize the .gitignore file. As it is now, it will ignore the directories mentioned above, the standard python files you don't want to track, and the usual latex files you don't want to track.\n")

print("You will be ask now for the path to your remote folder.\n")

time.sleep(3)

target_dir = input('Please provide the absolute path to the remote directory in your system: ')
target_dir = target_dir.replace("'",'').replace('"','')

if not os.path.exists(target_dir):
    sys.exit('{0} was not found in your system. You may include the path by dragging the directory into the terminal, but you have to delate any extra space added at the end.'.format(target_dir))

os.symlink(target_dir,os.path.join('remote'))
os.makedirs(os.path.join('local','scripts'), exist_ok=True)
os.mkdir(os.path.join('local','data'))
os.mkdir(os.path.join('scripts'))
os.mkdir(os.path.join('tex'))
os.mkdir(os.path.join('tex','tables'))
os.mkdir(os.path.join('tex','figures'))
