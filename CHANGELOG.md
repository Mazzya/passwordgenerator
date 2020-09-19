# Change Log

## v2.2.4 - Sep. 19, 2020
**Fixed:**
- Script compatibility with different operating systems has been improved

## v2.2.3 - Sep. 18, 2020
**Added:**
- Secrets module
- Code documentation

**Changed:**
- The password generation system has been considerably improved, now they are much more secure and strong. The randomness factor is much higher and impossible to predict. 

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