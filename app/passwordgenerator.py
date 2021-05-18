#!/usr/bin/env python
# This script has been developed by Mazzya
# Github : https://github.com/Mazzya
# Repository address : https://github.com/Mazzya/passwordgenerator
# This script allows you to generate strong passwords and save them

import string
from io import open
from colorama import init, Fore, Style
import secrets
from datetime import datetime
import argparse
import random

VERSION = '3.4.3'
BANNER = f"""{Fore.CYAN}{Style.BRIGHT}
*****************************************************************************************************************
*     ______                                      _    _______                                                  *    
*    (_____ \                                    | |  (_______)                                _                *
*     _____) )____  ___  ___ _ _ _  ___   ____ __| |   _   ___ _____ ____  _____  ____ _____ _| |_ ___   ____   *
*    |  ____(____ |/___)/___) | | |/ _ \ / ___) _  |  | | (_  | ___ |  _ \| ___ |/ ___|____ (_   _) _ \ / ___)  *
*    | |    / ___ |___ |___ | | | | |_| | |  ( (_| |  | |___) | ____| | | | ____| |   / ___ | | || |_| | |      *
*    |_|    \_____(___/(___/ \___/ \___/|_|   \____|   \_____/|_____)_| |_|_____)_|   \_____|  \__)___/|_|      *
*                                                                                                               *
*   Developed by Mazzya                                                                                         *
*   Version {VERSION}                                                                                               *
*   Github : github.com/Mazzya                                                                                  *
*   mazzya.tk                                                                                                   *
*****************************************************************************************************************                    
"""


class Password:

    current_version = "3.4.3"
    CHARS = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-9])

    def __init__(self, length):
        self.length = length
    
    def GeneratePassword(self):
        """ This function generates strong passwords with the character length that the user wants. """
        random.shuffle(Password.CHARS)
        return ''.join([
            secrets.choice(Password.CHARS) for _ in range(self.length)
        ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l',
        '--length',
        help='Length of password',
        type=int,
        default=4
    )

    parser.add_argument(
        '-n',
        '--number',
        help='specify how many password you need',
        default=1,
        type=int
    )
    args = parser.parse_args()

    for _ in range(args.number):
        print(Password(args.length).GeneratePassword())
