# pybatch
# github.com/sbritorodr/pybatch
# This program executes any instruction for all files inside a folder 
# (e.g. convert all these mp4 files into mkv using ffmpeg)

# the idea is to take, for example:
# ffmpeg -i [i] [o]
# sustitute input for each instance and generate an output with the same 
# name inside an ./output folder

# Title screen
print('''
            ______       _       _     
            | ___ \     | |     | |    
 _ __  _   _| |_/ / __ _| |_ ___| |__  
| '_ \| | | | ___ \/ _` | __/ __| '_ \ 
| |_) | |_| | |_/ / (_| | || (__| | | |
| .__/ \__, \____/ \__,_|\__\___|_| |_|
| |     __/ |                          
|_|    |___/                           

Make orders automatically
github.com/sbritorodr/pybatch
''')
import os
# help function
def help():
    print(
    '''
    This program needs a command, an input [i] and output [o]
    For example, in order to convert some files in ffmpeg you 
    need to write this:

    ffmpeg -i [i] [o].mkv
    ''')
# get working directoy
pwd = os.path.dirname(os.path.abspath(__file__))

# get folder:
input_folder = str(input("Add your folder path or leave it blank to select \"./ \": \n")) or "./"
print("You selected this folder: " + input_folder)

directory = pwd
if input_folder.startswith('.'):
    input_folder = input_folder.replace('.', '')
    directory += input_folder
elif input_folder.startswith('/'):
    directory = input_folder
print(directory)
# select file type:
file_type = str(input("select file type (.txt, .pdf, .rar...)")) or ""
print("you selected \"" + file_type + "\"")

# delete all whitespaces
def remove_whitespaces(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '_')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '_')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name

remove_whitespaces(directory)

# Loop to get all files
list_files = []
for file in os.listdir(directory):
    if file.endswith(file_type):
        list_files.append(file)
print(list_files)

# check if you mess up something
if list_files == []:
    raise Exception("No files are selected. Check if you have some files or you input folder exists")

# command string. It substitutes the [i] selection and the [o] with the algorithm

command = str(input("Add your command here. Write h if you need help:\n" )) or "ffmpeg -i [i] [o].mp3"
command_def = command # save the variable anywhere for the "main" loop
if command == 'h':
    help()
elif "[i]" not in command:
    raise Exception("you didn't add [i] or [o].")
if '[o]' in command:
    try: os.mkdir("output")
    except: 0

# Command loop with [i] and [o] replacement
for file in list_files:
    command = command_def
    output_file = file.split('.', 1)[0] # remove the file extension, to avoid '.mp4.mp3' gibberish
    command = command.replace('[i]', directory + file) 
    if "[o]" not in command:
        command = command.replace('[o]', "")
    else: 
        command = command.replace('[o]', pwd + "/output/" + output_file)
    print(command)
    os.system(command)
# End message
print("\n \n Script finished with no errors. If something has gone wrong, check if you write the command correctly")