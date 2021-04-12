from user import User
# from credentials import Credentials

def function():
    print("Welcome to Pass-Lock")

function()

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user
def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()
def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)

def main():
    print("Hello...\n nu ---  Create New Account  \n li ---  Have An Account  \n")
    if short_code == "nu":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" op - To type your own pasword:\n gp - To generate random Password")
        def passlocker():
    print("Hello Welcome to your Accounts Password Store...\n Please enter one of the following to proceed.\n nu ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "nu":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" tp - To type your own pasword:\n gp - To generate random Password")
            # password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
    else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Voila! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("*"*50)
        print("Key in Name and Password:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Pass-Lock")  
            print('\n')
    while True:
        print("Enter:\n nc - New Credential \n sc - Display Credentials \n fc - Find a credential \n gc - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
    
        if short_code == "nc":
            print("New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Username")
            userName = input()
            while True:
                print(" tp - To type your own pasword:\n gp - For random Password")
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
            elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("Credentials Unavailble")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Success..Proceed to Account")
        elif short_code == 'ex':
            print("Adios!")
            break
        else:
            print("Invalid Details..Try AGain")
    else:
        print("Enter Valid Data")

    
if __name__ == '__main__':
    main()