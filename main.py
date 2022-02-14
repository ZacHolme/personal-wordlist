# Used for command line
import sys
import string

'''
--------------------------------------------------------
Created by Zach Holme, Luke Willimott and Nathan Brown
personalWordlist v0.1
--------------------------------------------------------
'''


class Profile:
    """All the victims personal info to shape the Wordlist"""
    # Known personal info
    firstname = str
    lastname = str
    dob = int
    house_number = int
    city = str
    # This could include any other unique data collected. e.g. dog name, or unique id or code
    additonal_info = str

    def create(self):
        """Creates users profile instance"""
        print('Victims Details: ')
        self.firstname = input('First Name: ')
        self.lastname = input('Last Name: ')
        self.dob = input('Date of Birth (DD/MM/YYYY): ')
        self.house_number = input('House Number: ')
        self.city = input('City: ')
        self.additonal_info = input('Any other additional information: (E.g. dog name) ')
        return self


def gen_list(profile: Profile) -> string:
    # function for generating wordlist
    ...
    return 0


def main() -> string:
    ...
    new_profile: Profile = Profile()
    Profile.create(new_profile)
    checker = False
    """Checks for false input and gives a wordlist selection for the user"""
    while not checker:
        wordlist = input(
            f'(1) - Short wordlist\n(2) - Medium wordlist\n(3) - Long wordlist\nPick one of the following: ')
        if wordlist == '1':
            checker = True
        elif wordlist == '2':
            checker = True
        elif wordlist == '3':
            checker = True
        else:
            print('Incorrect input')
            checker = False

    return 0


if __name__ == '__main__':
    main()
