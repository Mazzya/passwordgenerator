import random
import string
import time
from io import open


def GeneratePassword():
    password = ""
    """ Creation of the variable where the generated password is stored """

    chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-6])

    try:

        length = int(input("How many characters do you want the password to have ?: "))

        for i in range(length+1):
            password += random.choice(chars)

        print(f"Password generated successfuly : {password}")

        time.sleep(0.5)
        
        choice = input("Do you want save this password in a file ? (Yes or No): ")

        if (choice.lower() == "yes"):
            file = open("password.txt", "w")
            file.write(f"Developed by https://github.com/Mazzya\n\nPassword : {password}".center(50, " "))
            file.close()
            print("File saved successfully")
        elif (choice.lower() == "no"):
            print("Bye !")
        else:
            print("Remember that you can only answer yes or no")

    except ValueError:
        """If the user enters a letter or float instead of an integer"""
        print("You have to enter an integer")
    except:
        print("Something is wrong...")