# Password Generator

**Version 2.2.3** - [Change log](CHANGELOG.md)

An incredible script capable of generating very secure passwords


### Requirements
```
Python 3
string
io
secrets
```
### How to use
```
import passwordgenerator
passwordgenerator.GeneratePassword()
```

The script will ask you how many characters you want the password to contain
```
>>> How many characters do you want the password to have ?: 8
```

When you have entered the number, a password is automatically generated
```
>>> Password generated successfuly : password
```

You can save the password in a text file so as not to lose it
```
>>> Do you want save this password in a file ? (Yes or No): Yes
>>> File saved successfuly
```
The file is saved in the same folder where you are using the module
