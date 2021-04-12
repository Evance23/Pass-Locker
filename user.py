import random

class User:
    

    user_list = [] #empty user list

    def __init__(self, user_name,password):
        self.user_name = user_name
        self.password = password
        #save new user
    def save_user(self):

        User.user_list.append(self)

    def delete_user(self):
       
        #removing a user from the list
        User.user_list.remove(self)


    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)
       


