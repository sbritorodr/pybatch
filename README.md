# PyBatch
A easy to use python script that can batch all files inside a folder

For example, with this script you can run ffprobe with all files inside this folder, or run ffmpeg y convert all files into any desired format

## Installation:
1. Download pybatch.py either by git clone or downloading through the releases tab
2. Place the file inside your working directory

## Usage
The program tells step by step how to select the format, the directory and the command
### Directory selection
As soon as you execute `pybatch.py`, the script will prompt this:

`Add your folder path or leave it blank to select "./input ":`

The directory must be given as full path or relative path:
* Full path example: `/usr/user/input/` it must start with "`/`"
* Relative path example: `./input`it must start on a period

### File extention selection
You need to select your file type. If you don't type anything it will select all files inside the folder

You should provide the file extension starting with a period:

`.txt`, `.pdf`, `.mp4`...

### Command input
If you type "h", a help screen will pop out if you don't remember the syntax
You need to write you batch command using a speciffic syntax. For example:

`ffmpeg -i [i] [o].mp3`

Whether "`[i]`" is the input parameter and the "`[o]`" is the output parameter
You don't have to add the output parameter if you don't need it in the command, but the input parameter is mandatory. 

For example: `ffprobe -i [i]`

| :exclamation:  | If your files has spaces in the name, it will be replaced with underscores   |
|---------------| :--------------------------|


By default, your files will be stored in ./output
