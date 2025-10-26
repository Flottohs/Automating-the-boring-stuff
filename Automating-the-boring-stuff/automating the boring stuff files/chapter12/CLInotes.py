
#USING TERMINAL


# You can see this CWD as part of the terminal prompt, or view it by running pwd (for print working directory) on macOS


#you can change the CWD in python using os.chdir(), or in the terminal using the cd command with either a relative or absolute path:

## go to the desktop folder
#cd ~/Desktop

# go up one directory
#cd ..

# go to a specific absolute path
#cd /System/Library


#to list files in a directory:
#ls          # list files in the current directory
#ls -l       # list with details like permissions, size, date
#ls -a       # include hidden files starting with .

#to list all executable files in your cwd:file * | grep executable

#once you are in the foler containing a program run it by doing ./example


#The PATH enviroment variable


#All running programs, no matter the language they’re written in, have a set of string variables called environment variables. One of these is the PATH environment variable-hich contains a list of folders the terminal checks when you enter the name of a program.


#To check the contents of you Path enviroment variable - run echo $Path
#this gives you;/Library/Frameworks/Python.framework/Versions/3.13/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin   

#Path editing
#To add folders to the PATH environment variables, you’ll need to edit the terminal startup script. This is the .zshrc file on macOS
# Both of these files are in your home folder and contain commands that are run whenever a new terminal window is opened. 
# On macOS, add the following to the bottom of the .zshrc file:
#export PATH=/Users/al/Scripts:$PATH


#which and where can be used to learn more about your files

#which python3 can tell you what version you have of python

#where python3 will tell you the path


#Virtual enviroment

#Say you have two Python programs, one that uses version 1.0 of a package and another that uses version 2.0 of that same package. Python can’t have two versions of the same package installed at the same time. If version 2.0 is not backward compatible with version 1.0, you’d be uninstalling one version and reinstalling the other each time you wanted to switch programs to run.

#Python’s solution to this problem is virtual environments; separate installations of Python that have their own set of installed third-party packages.

#To create a virtual environment, cd to your Scripts folder and run python –m venv .venv (using python3 on macOS)

#cd Scripts
#python -m venv .venv

#This creates the virtual environment’s files in a new folder named .venv
#Files and folders whose names begin with a period are hidden
#To use the virtual environment’s Python version, you must activate it. 

#The equivalent script on macOS and Linux is /Documents/programming/.venv/bin/activate, but due to security permissions, you can’t directly run it. Instead, run the command source activate:


#cd .venv/bin
#source activate
#which python3


#Activation changes the PATH environment variable so that python or python3 runs the Python interpreter inside the .venv folder instead of the original one. 
# It also changes your terminal prompt to include (.venv) so that you know the virtual environment is active. 
# Running which python3 in the activated virtual environment shows that python3 runs the Python interpreter in the newly created .venv/bin folder. 

# These changes apply to the current terminal window only; any existing or new terminal windows won’t have these environment variable or prompt changes. 
# This fresh Python installation has only the default packages, 
# and none of the packages you may have already installed in the original Python installation. 
# You can confirm this by running python –m pip list to list the installed packages:

#python -m pip list


#The standard practice is to create a virtual environment for each Python project you’re working on, since every project could have its own unique package dependencies. 
#To deactivate the virtual environment, deactivate (on macOS and Linux) in the same folder as the activate script. You can also simply close the terminal window and open a new one. If you want to permanently delete the virtual environment along with its installed packages, just delete the .venv folder and its contents.

#deactivate



#installing python packages with pip

#python3 –m pip install package_name


#to list all packages:
#python3 –m pip list


#python3 –m pip install automateboringstuff3


#Self-Aware Python Programs


#The sys.executable variable contains the full path and file of the Python interpreter program itself, and the sys.version variable contains the string that appears at the top of the interactive shell with version information about the Python interpreter.

#The sys.version_info.major and sys.version_info.minor variables contain integers of the major and minor version numbers of the Python interpreter. On my laptop running Python version 3.13.1, these are 3 and 13, respectively. You can also pass sys.version_info to the list() function to obtain more specific information: list(sys.version_info) returns [3, 13, 1 'final', 0] on my laptop. Having the version information in this form is much easier to work with than trying to pull it out of the sys.version string.

#The os.name variable contains the string 'nt' if running on Windows and 'posix' if running on macOS or Linux. This is useful if your Python script needs to run different code depending on what operating system it’s running on.

#For more specific operating system identification, the sys.platform variable contains 'win32' on Windows, 'darwin' on macOS, and 'linux' on Linux.


#If you need highly specific information about the OS version and type of CPU, the built-in platform module can retrieve this information. This module is documented online at https://docs.python.org/3/library/platform.html.


# If you need to check whether a module is installed, put the import statement in a try block and catch the ModuleNotFoundError exception:
'''
try:
    import #nonexistentModule
except ModuleNotFoundError:
    print('This code runs if nonexistentModule was not found.')
'''



    
#Text-Based Program Design


#Short Command Names- good as there easier to type, easy to understand

#command line arguments

#The bit of text supplied after a command is called a command line argument.
#Command line arguments are passed to commands in much the same way as arguments to a function call. For example, the ls command by itself lists the files in the CWD
#Python scripts can access the command line scripts given to the Python interpreter from the sys.argv list.
#For example, if you entered python3 yourScript.py hello world, the python3 program would receive the command line arguments and forward them to your Python script in the sys.argv variable. The sys.argv variable would contain ['yourScript.py', 'hello', 'world'].


#The main usefulness of command line arguments is that you can specify a wide variety of configurations before you start the program. There’s no need to go through a configuration menu or multistep process. 
#use help to find command line arguments

#However, as you add more command line arguments, the possible combinations can become cumbersome to manage. Should python yourScript.py spam eggs do the same thing as python yourScript.py eggs spam? If the user can have either a cheese argument or a bacon argument, what happens if they provide both? This complexity would require you to write a lot of code to handle the various edge cases. At this point, you’re probably better off using Python’s built-in argparse module to handle these complicated situations. 

#Clipboard I/O

#pyperclip
#pyperclip.copy()
#pyperclip.paste()



#Colourful text with BEXT
import bext

#Bext only works in programs run from a terminal window, and not from Mu or most other code editors. To have print() produce colorful text, call the fg() and bg() functions to change the (foreground) text color or the background color with a string argument such as 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'purple', 'cyan', or 'white'. You can also pass 'reset' to change the color back to the terminal window’s default color. For example, enter the following into the interactive shell:

bext.fg('red')
print('This text is red.')
bext.bg('blue')
print('Red text on blue background is an ugly color scheme.')
bext.fg('reset')
bext.bg('reset')
print('The text is normal again. Ah, much better.')

#bext.clear() Clears the screen

#bext.width() and bext.height() Returns the current width (in columns) and height (in rows) of the terminal window, respectively

#bext.hide() and bext.show() Hides and shows the cursor, respectively

#bext.title(text) Changes the title bar of the terminal window to the text string

#bext.goto(x, y) Moves the cursor to column x and row y in the terminal, where 0, 0 is the top-left position

#bext.get_key() Waits for the user to press any key and then returns a string describing the key



#Terminal clearing

import os
def clear():
    os.system('cls' if os.name =='nt' else 'clear')
    
    #This code lets your program clear the terminal screen without requiring the installation of the Bext package and only works in Python scripts run from the terminal, not from Mu or another code editor. 
    
    
    
    
#Sound and text notifications
from pathlib import Path
print(os.getcwd())
import playsound3

playsound3.playsound('hello.mp3')


#pop up message boxes with pymsgbox
import pymsgbox

#you can add small GUI message boxes to your program with the PyMsgBox package

pymsgbox.alert('meow')
#Displays a text message until the user clicks OK, then returns the string 'OK'

pymsgbox.confirm('reef')
#Displays a text message until the user clicks OK or Cancel, then returns 'OK' or 'Cancel'

pymsgbox.prompt('cars')
#Displays a text message along with a text field, then returns the text the user entered as a string or None if they clicked Cancel

pymsgbox.password('inputpasswordgng')
#Is the same as pymsgbox.prompt(), but the text the user enters is masked by asterisks



#Deploying python programs

#Pressing the COMMAND key and the spacebar simultaneously on macOS brings up Spotlight, allowing you to enter the name of a program to run. To add your own Python scripts to Spotlight, you must do the following:

#1.  Place the yourScript.py Python script in your Scripts folder.

#2.  Create a text file named yourScript.command to run the Python script.

#3.  Run chmod u+x yourScript.command to add execute permissions to the yourScript.command file.

#Once you have your .py Python script in your Scripts folder, such as /Users/al/Scripts, create a text file named yourScript.command in the Scripts folder with the following content:

#source ~/Scripts/.venv/bin/activate
#python3 ~/Scripts/yourScript.py
#deactivate

#Finally, in a terminal, cd to ~/Scripts and run the command chmod u+x yourScript.command. 
# This adds execute permissions so that you can run the script from Spotlight. Now you’ll be able to quickly run the Python script by pressing ⌘-spacebar and entering yourScript.command.
# (Spotlight should autocomplete the full name for you after you enter the first few characters.) 
# You’ll also be able to run your Python script from the terminal by entering yourScript.command.


# Compiling Python Programs with PyInstaller

# Python is often called an interpreted language, but that just means
# its code normally runs through the Python interpreter instead of being
# compiled directly into machine code. However, you can still create a
# standalone executable version of your Python script using PyInstaller.

# PyInstaller bundles:
#  - your Python script
#  - a copy of the Python interpreter
#  - any required modules
# into a single executable file that can run on another computer
# even if Python isn’t installed.

# Because the interpreter is included, these executables are large
# (even a simple "Hello world" program can be 8–10 MB), but the benefit
# is that you can share your program easily.

# --------------------------------------------------------------
# Installing PyInstaller
# --------------------------------------------------------------
# Install it in your current environment (venv or global):
# python3 -m pip install pyinstaller

# PyInstaller must be run on the same operating system you want
# the executable to run on:
#   - macOS → builds a macOS executable
#   - Windows → builds a .exe
#   - Linux → builds a Linux binary
# You cannot make a Windows .exe from macOS, and vice versa.

# --------------------------------------------------------------
# Creating an Executable on macOS
# --------------------------------------------------------------
# Navigate to the folder containing your Python file, then run:
# python3 -m PyInstaller --onefile yourScript.py
#
# Notes:
#  - PyInstaller is case sensitive (capital P and I)
#  - The --onefile flag bundles everything into a single executable

# Example terminal output:
# 123 INFO: PyInstaller: 6.3.0
# 123 INFO: Python: 3.13.0
# 125 INFO: Platform: macOS-14.3-arm64
# --snip--
# 3000 INFO: Building EXE from EXE-00.toc completed successfully.

# --------------------------------------------------------------
# After Running PyInstaller
# --------------------------------------------------------------
# PyInstaller creates two folders in the same directory as your script:
#  - build/ : temporary build files (you can delete this)
#  - dist/  : contains the final executable
#
# Example:
# dist/yourScript
#
# You can run the compiled program from the terminal:
# ./dist/yourScript
#
# Or double-click it in Finder (you may need to allow it in
# System Settings > Privacy & Security the first time).

# --------------------------------------------------------------
# Notes
# --------------------------------------------------------------
# - You don’t need a virtual environment specifically for PyInstaller.
# - The executable can be shared or emailed (though some email
#   providers block executables for security).
# - For more advanced options, see the official docs:
#   https://pyinstaller.org
