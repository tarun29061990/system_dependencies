# README #

### What is this repository for? ###

This is a system dependencies management application.

### How do I get set up? ###

This project uses python3. You need to have 
python3.6 virtual environment installed on your machine.
To install python3.6 virtual environment follow this link:
 
https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 

After installing the virtual environment, go to the project folder and type: 

    source <virtual_env_directory> activate
    
Run the application by typing:
    
    python src/main.py

After running the application    
output will be written in output.txt file
for testing with other inputs try to modify input.txt file located in the root folder of the project.

### How to run tests
Test cases are located in tests folder.
In order to run the test cases simply type:
    Due ot shortage of I couldn't able to write tests

### Project Structure and Logic

The whole code lies in the src folder.
1. main.py - This is the main starting file of the application. It register users, create a user graph and sort the edges based on parameters.

2. commands directory - This handles all the code related to operations namely install, depend, remove, list.


### Who do I talk to? ###

* Tarun Chaudhary (http://curioustechie.in)