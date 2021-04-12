import unittest
from credentials import Credentials
from user import User

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('ChuorNyagot','BvB6ghp2')

    def test_init(self):
        """
        test case to chek initialization
        """
        self.assertEqual(self.new_user.username,'ChuorNyagot')
        self.assertEqual(self.new_user.password,'BvB6ghp2')

    def test_save_user(self):
        """
       Testing if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    Defining test cases for credentials class
    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('IG','Evance23','ab4Fb23')
    def test_init(self):
        """
        Test case for Initialization of credentials
        """
        self.assertEqual(self.new_credential.account,'IG')
        self.assertEqual(self.new_credential.userName,'Evance23')
        self.assertEqual(self.new_credential.password,'ab4Fb23')

    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)
     def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Tinder","De Mabior","bgh67tr") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
     def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Tinder","De Mabior","bgh67tr")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
     def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()
