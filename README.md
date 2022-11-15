# Command Geometry Playground
## Intro
This project is a command lined based software written in Python 3 which is used to demonstrate geometry principles including congruence, area, primeter, etc.. 
## Usage
To use this project, you must compile a executable by using a PyPI module named pyinstaller from this source codes. However, in order to simplify this process, a Makefile is used to speed up this process of compiling. You have to make sure that GNU make is properly installed on to your build machine and been added to either PATH or Enviroment Variable. If you did not install the required software(s), please follow the guide in "Compile"
This project is a command line based software thus, you may not use your mouse or touchpad to interact with this application. the commands that you will use is defined and explained below:
## Compile
To compile this project from source, you must install GNU Make prior to compile. For Microsoft Windows® users, please go to https://chocolatey.org/install and install `choco` and type command: `choco install make` and macOS® users may run command: `chmod u+x get_make.sh && sh get_make.sh`or use other package manage tool such as brew. 
After installing the required tools, use Makefile to compile this from source to a executable.
1. Make base configuration
a. type command in to administrator shell: `make <os_name>_config`
2. Build executable
a. type command into administrator shell: `make exec`
## Run Executable
After compiling to executable, you may found the file under /dist folder. Double click on that or run `dist/Geo_Playground.exe` on Windows® or `cd dist && ./Geo_Playground`. 
