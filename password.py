import random
from user import user



def main ():
    

    while True:
        print("Good to see You!!!")
        print('\n')
        print("To create new user use 'nu': to log in use 'lg" or 'ex' to exit")
        short_code = input().lower()
        print('\n')

        if short_code == "nu" :
            print("create username")
            created_user_name = input()

            print ('create password')
            created_user_password