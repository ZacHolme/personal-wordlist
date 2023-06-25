# Used for command line
import sys
import string

'''
--------------------------------------------------------
Created by Zach Holme
personalWordlist v0.1
--------------------------------------------------------
'''

import sys
import random
import os
from itertools import permutations
import argparse


class Profile:
    """All the victim's personal info to shape the wordlist"""
    # Known personal info
    firstname = str
    lastname = str
    dob = str  # Changed data type to string for easier manipulation
    house_number = int
    city = str
    # This could include any other unique data collected. e.g. dog name, or unique id or code
    additional_info = []

    def create(self):
        """Creates user's profile instance"""
        print('Victim\'s Details: ')
        self.firstname = input('First Name: ')
        self.lastname = input('Last Name: ')
        self.dob = input('Date of Birth (DD/MM/YYYY): ')
        self.house_number = input('House Number: ')
        self.city = input('City: ')
        additional_info_input = input('Any other additional information (E.g. dog name): ')
        self.additional_info = [info.strip() for info in additional_info_input.split(',') if info.strip()]
        return self


def generate_wordlist(profile: Profile, wordlist_type: int) -> list:
    wordlist = []
    components = ['!', '@', '#', '$', '%', '&', '_', '123','1234']
    random.shuffle(components)

    firstname = profile.firstname
    lastname = profile.lastname
    dob = profile.dob
    house_number = profile.house_number
    city = profile.city
    additional_info = profile.additional_info

    dob_parts = dob.split('/')
    day = dob_parts[0]
    month = dob_parts[1]
    year = dob_parts[2]

    if wordlist_type == 1:
        wordlist_length = 200
    elif wordlist_type == 2:
        wordlist_length = max(500, 2 * len(firstname) * len(lastname) * len(components))
    elif wordlist_type == 3:
        wordlist_length = max(2000, 3 * len(firstname) * len(lastname) * len(components))
    else:
        return wordlist

    max_attempts = 1000
    attempts = 0

    while len(wordlist) < wordlist_length and len(wordlist) < 2000 and attempts < max_attempts:
        random_component = random.choice(components)

        words = [
            firstname.lower(),
            firstname.title(),
            lastname.lower(),
            lastname.title(),
            day,
            month,
            year,
            year[-2:],
            house_number,
            city.lower(),
            city.title()
        ]

        for r in range(2, len(additional_info) + 1):
            additional_info_perms = permutations(additional_info, r)
            for perm in additional_info_perms:
                words.append(''.join(perm).lower())
                words.append(''.join(perm).title())

        random.shuffle(words)
        words.sort(key=lambda x: (len(x), x))

        for word in words:
            password = word + random_component
            if len(password) >= 6 and len(password) <= 14 and password not in wordlist:
                wordlist.append(password)
                if len(wordlist) == wordlist_length or len(wordlist) == 2000:
                    break

        attempts += 1

    approx_passwords = len(wordlist) * (max_attempts // attempts)

    passwords_without_numbers = [
        password + random.choice(components)
        for password in wordlist
        if not any(char.isdigit() for char in password)
    ]
    wordlist.extend(passwords_without_numbers)

    random.shuffle(wordlist)
    wordlist = wordlist[:wordlist_length]

    return wordlist, approx_passwords


def main():
    parser = argparse.ArgumentParser(description='Wordlist Generator')
    parser.add_argument('-t', '--type', type=int, choices=[1, 2, 3], default=3,
                        help='Type of wordlist to generate (1 - Small, 2 - Medium, 3 - Long)')
    args = parser.parse_args()

    new_profile = Profile()
    new_profile.create()

    wordlist, approx_passwords = generate_wordlist(new_profile, args.type)

    # Save wordlist to a text file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = input(f"Enter the file path to save the wordlist (default: {script_directory}/wordlist.txt): ")

    if not file_path:
        file_path = os.path.join(script_directory, "wordlist.txt")

    with open(file_path, 'w') as file:
        file.write('\n'.join(wordlist))

    print(f"Wordlist has been generated and saved to {file_path}")

    print(f"Approximate number of generated passwords: {approx_passwords}")
    print(f"Generated password list: {'Small Wordlist' if len(wordlist) <= 200 else ('Medium Wordlist' if len(wordlist) <= 1000 else 'Long Wordlist')}")


if __name__ == '__main__':
    main()
