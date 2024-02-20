#!/usr/bin/env python
# This program has been developed by Mazzya
# Github : https://github.com/Mazzya
# Project repository : https://github.com/Mazzya/passwordgenerator
# Generate passwords in a fast and secure way !

import string
import time
from io import open
from colorama import init, Fore, Style
import secrets
from datetime import datetime

VERSION = '4.0.0'
BANNER = f"""{Fore.CYAN}{Style.BRIGHT}

     ______                                      _    _______                                                     
    (_____ \                                    | |  (_______)                                _                
     _____) )____  ___  ___ _ _ _  ___   ____ __| |   _   ___ _____ ____  _____  ____ _____ _| |_ ___   ____   
    |  ____(____ |/___)/___) | | |/ _ \ / ___) _  |  | | (_  | ___ |  _ \| ___ |/ ___|____ (_   _) _ \ / ___)  
    | |    / ___ |___ |___ | | | | |_| | |  ( (_| |  | |___) | ____| | | | ____| |   / ___ | | || |_| | |      
    |_|    \_____(___/(___/ \___/ \___/|_|   \____|   \_____/|_____)_| |_|_____)_|   \_____|  \__)___/|_|      
                                                                                                               
   Developed by Mazzya                                                                                         
   Version {VERSION}                                                                                           
   Github : https://github.com/Mazzya

"""


class Password:

    dt = datetime.now()

    def __init__(self):
        self.generate_password()

    def check_password_name(self, password_name) -> bool:
        """ This function checks if the user has entered a password name """
        is_valid = False
        if password_name != "":
            is_valid = True
        return is_valid

    def generate_password(self):
        """ This function generates strong passwords with the character length that the user wants. """

        init(autoreset=True)

        chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-9])

        try:

            print(BANNER)

            length = int(input("How many characters do you want the password to have ?: "))

            # If the user enters 4 characters or more, the password is generated
            if length >= 4:
                # Creation of the variable where the generated password is stored
                password = ""

                for i in range(length): password += secrets.choice(chars)

                # The generated password is displayed next to a message
                print(f"{Fore.GREEN}{Style.BRIGHT}Password generated successfully : {password}\n")

                # Asks the user if they want to save the password to a file.
                choice = input("Do you want save this password in a file ? (Yes or No): ")

                self.core(choice, password)
                
            # If the user enters less than 4 characters, the password is not generated
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Enter a minimum of 4 characters")

        except ValueError:
            # If the user enters a letter or float instead of an integer
            print(f"{Fore.RED}{Style.BRIGHT}You have to enter an integer")

        except PermissionError:
            # If the file does not contain the necessary permissions to be able to write to it
            print("Permission denied, check file permissions")

        except Exception as e:
            print(f"{Fore.RED}{Style.BRIGHT}Something is wrong...")
    
    def save_password(self, password_name: bool, password):
        if self.check_password_name(password_name):
            with open('password.txt', 'a+') as f:
                f.write(f"{password_name} password : {password} --- ({self.dt.day}/{self.dt.month}/{self.dt.year})" + "\n")
                print(f"{Fore.GREEN}{Style.BRIGHT}File saved successfully")
        else:
            with open('password.txt', 'a+') as f:
                f.write(f"password : {password} --- ({self.dt.day}/{self.dt.month}/{self.dt.year})" + "\n")
                print(f"{Fore.GREEN}{Style.BRIGHT}File saved successfully")
    
    def core(self, choice: str, password):
        while True:
                    # If the user wants to save the password in a file.
                    if choice.lower() == "yes":
                        password_name = input("Password name (If you don't want to give it a name, press enter): ")
                        self.save_password(password_name, password)
                        break

                    # If the user don't wants to save the password in a file.
                    elif choice.lower() == "no":
                        print(f"{Fore.BLUE}{Style.BRIGHT}Closing...")
                        time.sleep(1)
                        break

                    # If the user enters another word that is neither 'yes' nor 'no'
                    else:
                        print(f"{Fore.RED}{Style.BRIGHT}Remember that you can only answer yes or no")
                        choice = input("Do you want save this password in a file ? (Yes or No): ")


if __name__ == "__main__":
    core = Password()
