# Change Log
## v3.4.3 - Mar. 07, 2021
**Added:**
- Password name : Naming the passwords can be very useful when we have many, so now it is possible to name the passwords that you are going to generate, the objective is to facilitate the organization of the passwords.
## v3.3.3. - Feb. 07, 2021
**Added:**
- Datatime module : When the user generates a password, the date the password was generated will also be seen, the objective is for the user to know when the password was generated
- A script entry point has been added.

**Changed:**
- The structure of the code
- The script no longer serves as a simple module, now it only works as a script that can be run in any environment. We noticed that it was not suitable to be a module to use in development. The main idea of this project has always been to create an easy to use mini program capable of generating strong and secure passwords.

**Removed:**
- The file __init__.py has been removed, this file told Python that it was a module.
## v2.3.3 - Sep. 20, 2020
**Added:**
- Colorama module
- The aesthetics of the text that is printed on screen has been improved by adding colors

**Changed:**
- A dynamic variable has been created where the version of the program has been saved, which will facilitate its manipulation in the future
- The file saving system has been improved

## v2.2.3 - Sep. 19, 2020
**Added:**
- Secrets module
- Code documentation
- Code cleaned

**Changed:**
- The password generation system has been considerably improved, now they are much more secure and strong. The randomness factor is much higher and impossible to predict. 

**Fixed:**
- Script compatibility with different operating systems has been improved

**Removed:**
- Random module

## v1.1.2 - Sep. 16, 2020
**Added:**
- Character verification : if the user enters less than 4 characters he will not be able to generate a password
- Developer contact information added in script source code
- Requirements to use the script without problems

**Changed:**
- When the user generates a password and saves it in a text file, wanting to generate another password, the old one is deleted and the new one appears. Now instead of replacing the existing content, the new password is saved on the next line. This allows users to keep track of all generated passwords.

**Removed:**
- The function that centered the text in the generated text file has been removed
- Time module

## v0.0.1 - Sep. 15, 2020

Initial relase.

**Added:**
- Change Log
- Time module