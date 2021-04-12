    import random

    from user import User 


def main():

    while True:
        print("Good to see You!!!")
        print('\n')
        print("to create new user use 'nu': to log in use 'lg' or 'ex' to exit")
        short_code = input().lower()
        print('\n')

        if short_code == "nu":
            print("create username")
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('validate!')
            validate_password = input()

            while validate_password  != created_user_password:
                print("password did not match!")
                print("enter password")
                created_user_password = input()
                print("validate password")
                validate_password = input()
            else:
                print(f"welcome {created_user_name}! account created successfully")
                print('\n')
                print("log in")
                print("Username")
                entered_username = input()
                print("enter password")
                entered_password = input()
            while entered_username != created_user_name or entered_password != created_user_password:
                print("Invalid log ins")
                print("Username")
                entered_username = input()
                print("enter password")
                entered_password = input()
            else:
                print(f"Welcome: {entered_username} to your account")
                print('\n')

        elif short_code == 'lg':
            print("welcome")
            print("Username")
            default_user_name = input()
            

            print("Enter password")
            default_user_password = input()
            print('\n')
            while default_user_name != 'admin' or  default_user_password != '12345':
                print("Invalid username or password. Username 'admin' and password '12345'")
                print("Username")
                default_user_name = input()

                print("Enter password")
                default_user_password = input()
                print('\n')
            else:
                print("Log in successful")
                print('\n')
                print('\n')

        elif short_code == 'ex':
            break 
        else:
                print("enter valid code to continue")


if __name__ == '_main_':
    main()
