from cryptography.fernet import Fernet
import re
import ctypes
import time
import os
import sys


class Credentials()

     def __init__(self):
        self.__username = ""
        self.__key = ""
        self.__password = ""
        self.__key_file = 'key.key'
        self.__time_of_exp = -1

         @property
    def username(self):
        return self.__username
   
    @username.setter
    def username(self,username):
        while (username == ''):
            username = input('Enter a proper User name, blank is not accepted:')
        self.__username = username
   
    @property
    def password(self):
        return self.__password
   
    @password.setter
    def password(self,password):
        self.__key = Fernet.generate_key()
        f = Fernet(self.__key)
        self.__password = f.encrypt(password.encode()).decode()
        del f
   
    @property
    def expiry_time(self):
        return self.__time_of_exp
   
    @expiry_time.setter
    def expiry_time(self,exp_time):
        if(exp_time >= 2):
            self.__time_of_exp = exp_time
   
   
    def create_cred(self):
        

   
        cred_filename = 'CredFile.ini'
   
        with open(cred_filename,'w') as file_in:
            file_in.write("#Credential file:\nUsername={}\nPassword={}\nExpiry={}\n"
            .format(self.__username,self.__password,self.__time_of_exp))
            file_in.write("++"*20)

             if(os.path.exists(self.__key_file)):
            os.remove(self.__key_file)

            os_type = sys.platform
            if (os_type == 'linux'):
                self.__key_file = '.' + self.__key_file
   
            with open(self.__key_file,'w') as key_in:
                key_in.write(self.__key.decode())

                if(os_type == 'win32'):
                    ctypes.windll.kernel32.SetFileAttributesW(self.__key_file, 2)
                else:
                    pass
   
        except PermissionError:
            os.remove(self.__key_file)
            print("A Permission error occurred.\n Please re run the script")
            sys.exit()

            self.__username = ""
        self.__password = ""
        self.__key = ""
        self.__key_file
   