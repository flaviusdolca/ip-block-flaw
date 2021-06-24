
# Ip block flaw example ![Version](https://img.shields.io/badge/version-0.0.1-blue.svg) ![Python](https://img.shields.io/badge/Python-yellow?logo=python)
IP blocking is a tehnique against brute-force attacks. This tehnique consists in blocking the IP of a certain remote user if they make too many login attempts in quick succession.
This mechanism  in some cases could be vulnerable to bruteforce attacks.
For example, you might sometimes find that your IP is blocked if you fail to log in too many times. In some implementations, the counter for the number of failed attempts resets if the IP owner logs in successfully. This means an attacker would simply have to log in to their own account every few attempts to prevent this limit from ever being reached. 
This script is an example of this vulnerability.

## Run script
The scipts needs accepts 2 parameters, a mandatory URL parameter  and a passoword file wich is optional. By default there is a default password list used my the program if you don't specify a file.
### Usage
Without a password file:

       python main.py URL


With custom password file:

    python main.py URL myPassFile.txt



