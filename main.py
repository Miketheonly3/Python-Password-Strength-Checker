"""practice stuff """

from specif import *
from cryptography.fernet import Fernet

passwordInput = str(input("Enter Your Password: "))


def tryAgain():
    retry = input("Try again: ")
    check(retry)

def goodPassword(password):
    print("%s is the Perfect password! Now it is being encrypted" % password)
    encrypt(password)

def check(password):
    bad = False
    if len(password) < 5:
        print("The password '%s' is less the 5 characters" %(password))
        tryAgain()
        bad = True
    elif len(password) >= 15:
        print("The password '%s' is too long, and must be less than 15 characters" %(password))
        tryAgain()
        bad = True
    for x in (commonPasswords):
        if str(x).lower() in password.lower() and (len(password.lower()) - 8) < len(str(x).lower()):
            print("The password '%s' is too common" %(password))
            tryAgain()
            bad = True
            break
        else:
            continue
    for x in range(10):
        if not str(x) in password.lower():
            if x == 9 and not str(9) in password.lower():
                print("The password '%s' does not have at least one number" %(password.lower()))
                print(x)
                tryAgain()
                bad = True
        else:
            break
    for x in specialCharacters:
        if not str(x) in password.lower():
            if str(x) == "?" and not str(x) in password.lower():
                print("The password '%s' does not have a special character" %(password.lower()))
                print(x)
                tryAgain()
                bad = True
        else:
            break
    if password.upper() == password or password.lower() == password:
        print("The password '%s' does not have atleast one uppercase or one lowercase" %(password.lower()))
        print(x)
        tryAgain()
        bad = True
    if " " in password:
        print("The password '%s' cannot have any spaces" %(password.lower()))
        print(x)
        tryAgain()
        bad = True

    if bad == False:
        goodPassword(password)

def encrypt(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    password = fernet.encrypt(password.encode())
    print("Your password is now encrypted to %s" % password)
    decrypt = input("To decrypt, type D: ")
    if decrypt == "D":
        password = fernet.decrypt(password).decode()
        print("Now you got your password back! it was %s right?" % password)
        reEncrypt = input("To re-encrypt, Type E: ")
        if reEncrypt == "E":
            encrypt(password)
        elif not reEncrypt == "E":
            print("That was NOT E, now you gotta restart")
            passwordInput = str(input("Enter Your Password: "))
            check(passwordInput)
    elif not decrypt == "D":
        print("That was NOT D, now you gotta restart")
        passwordInput = str(input("Enter Your Password: "))
        check(passwordInput)


check(passwordInput)
