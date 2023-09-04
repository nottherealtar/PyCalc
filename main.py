from random import choice
from time import sleep
import string
import os

caps=list(string.ascii_uppercase)
lows=list(string.ascii_lowercase)
nums=[str(i) for i in range(10)]
spesChars=["!","@","#","$","%","^","&","*","|","/"]

def ProgInfo():
    authid = 'nottherealtar'
    lice = 'Apache2.0'
    name = 'PyCalc'
    lang = 'Python'
    language = 'en-US'
    stars = 420
    forks = 69
    vers = 1.0
    api = None
    lines = 150
    f = '/PyCalc/main.py'
    if os.path.exists(os.path.abs.path(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    desc = "Script for generating reliable Passwords!"
    print(f"[+] Author: {authid}")
    print(f"[+] Github: @{authid}")
    print(f"[+] Version: {str(vers)}")
    print(f"[+] Name: {name}")
    print(f"[+] Programming language: {lang}")
    print(f"[+] Natural language: {language}")
    print(f"[+] Description: {desc}")
    print(f"[+] Stars on Github repo: {str(stars)}")
    print(f"[+] Forks on the Github repo: {str(forks)}")
    print(f"[+] API used: {str(api)}")
    print(f"[+] Number of lines: {lines}")
    print(f"[+] File size: {str(fsize)} KB")
    print(f"[+] Path to file: {os.path.abspath(f)}")

def main():
    print("[+] Welcome to PyCalc")
    print("[+] Github: @nottherealtar")
    print("\n")
    print("[1] Generate Password's")
    print("[2] Show more info")
    print("[3] Exit")
    num=int(input("[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 3 or num == None:
        if num == None:
            print("[!] This field can't be blank !")
        else:
            print("[!] Invalid number !")
        print("[1] Generate password")
        print("[2] Display script's info")
        print("[3] Exit")
        num=int(input("[::] Please enter a number (from the above ones): "))
    if num == 1:
        cap=str(input("[?] Do you want to include capital letters ? [Y/N] "))
        while (cap != "y" and cap != "Y" and cap != "n" and cap != "N") or cap == None:
            print("[!] Invalid input !")
            sleep(1)
            cap=str(input("[?] Do you want to include capital letters ? [Y/N] "))
        if cap == "y" or cap == "Y":
            capital = True
        else:
            capital = False

        low=str(input("[?] Do you want to include lowercase letters ? [Y/N] "))
        while (low != "y" and low != "Y" and low != "n" and low != "N") or low == None:
            print("[!] Invalid input !")
            sleep(1)
            low=str(input("[?] Do you want to include lowercase letters ? [Y/N] "))
        if low == "y" or low == "Y":
            lower = True
        else:
            lower = False

        num=str(input("[?] Do you want to include numbers ? [Y/N] "))
        while num != "y" and num != "Y" and num != "n" and num != "N" or num == None:
            print("[!] Invalid input !")
            sleep(1)
            num=str(input("[?] Do you want to include numbers ? [Y/N] "))
        if num == "y" or num == "Y":
            numbers = True
        else:
            numbers = False

        speschar=str(input("[?] Do you want to include special characters ? [Y/N] "))
        while speschar != "y" and speschar != "Y" and speschar != "n" and speschar != "N"  or speschar == None:
            print("[!] Invalid input !")
            sleep(1)
            speschar=str(input("[?] Do you want to include special characters ? [Y/N] "))
        if speschar == "y" or speschar == "Y":
            specialchar = True
        else:
            specialchar = False

        length=int(input("[::] Please enter the password length: "))
        while length < 4:
            print("[!] Weak password !")
            sleep(1)
            length=int(input("[::] Please enter again length of the password: "))

        RANDLIST = []
        if capital:
            RANDLIST += caps
        if lower:
            RANDLIST += lows
        if numbers:
            RANDLIST += nums
        if specialchar:
            RANDLIST += spesChars
        psw = ""
        for i in range(length):
            psw += choice(RANDLIST)

        print(f"[✓] Generated Password: {psw}")
        sleep(2)
        print("[1] Return to menu")
        print("[2] Exit")
        number=int(input("[::] Please enter a number (from the above ones): "))
        while number < 1 or number > 2 or number == None:
            if number == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid number !")
            print("[1] Return to menu")
            print("[2] Exit")
            number=int(input("[::] Please enter again a number (from the above ones): "))
        if number == 1:
            main()
        else:
            print("[+] A calculator was a good idea")
            sleep(2)
            print("[+] See you next time 👋")
            sleep(1)
            exit(0)
    elif num == 2:
        ProgInfo()
    else:
        print("[+] A calculator was a good idea")
        sleep(2)
        print("[+] See you again 👋")
        sleep(1)
        exit(0)
        
if __name__ == '__main__':
    main()
