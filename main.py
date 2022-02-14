# Used for command line
import sys
import string

'''
Created by Zach Holme, Luke Willimott and Nathan Brown
personalWordlist v0.1
'''


class Profile:
    """All the victims personal info to shape the Wordlist"""
    # Known personal info
    firstname = str
    lastname = str
    house_number = int
    address = str
    # This could include any other unique data collected.
    additonal_info = str


def create_profile() -> string:
    """ This might as well be a class but for now I've just done a function boilerplate """
    new_profile = Profile()
    new_profile.firstname = input('First Name: ')
    new_profile.lastname = input('Last Name: ')
    new_profile.house_number = input('House Number: ')
    new_profile.address = input('Rest of Address (e.g. Preston Road)')
    new_profile.additonal_info = input('Any other additional information: ')
    return new_profile



def gen_list(user: string) -> string:
    # function for generating wordlist
    ...
    return 0


def main() -> string:
    ...
    # gen_list(profile())
    profile = create_profile()
    print(profile.firstname)
    return 0


if __name__ == '__main__':
    main()
