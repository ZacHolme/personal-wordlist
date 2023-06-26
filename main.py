import sys
import random
import os
import string
from itertools import permutations, combinations
import argparse


class Profile:
    """All the victim's personal info to shape the wordlist"""
    # Known personal info
    firstname = str
    lastname = str
    dob = []  # Changed data type to list for date of birth parts
    city = str
    # This could include any other unique data collected. e.g. dog name, or unique id or code
    additional_info = []

    def create(self):
        """Creates user's profile instance"""
        print('Victim\'s Details: ')
        self.firstname = input('First Name: ')
        self.lastname = input('Last Name: ')
        dob_input = input('Date of Birth (DD/MM/YYYY): ')
        self.dob = dob_input.split('/')
        self.city = input('City: ')
        additional_info_input = input('Any other additional information (E.g. dog name): ')
        self.additional_info = [info.strip() for info in additional_info_input.split(',') if info.strip()]
        return self


def generate_wordlist(profile: Profile, wordlist_type: int) -> list:
    wordlist = []
    components = ['!', '@', '#', '$', '%', '&', '_', '123', '1234']
    random.shuffle(components)

    firstname = profile.firstname
    lastname = profile.lastname
    dob = profile.dob
    city = profile.city
    additional_info = profile.additional_info

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
        words = [
            firstname.lower(),
            firstname.title(),
            lastname.lower(),
            lastname.title(),
            city.lower(),
            city.title()
        ]

        # Generate dob_parts without leading zeros
        dob_parts = [
            part.lstrip('0') + word
            for part in dob
            for word in random.sample(words, len(words) // 2)  # Use a subset of words to reduce frequency
        ]
        words.extend(dob_parts)

        for r in range(2, min(len(additional_info) + 1, 4)):
            additional_info_combinations = combinations(additional_info, r)
            for combo in additional_info_combinations:
                words.append(''.join(combo).lower())
                words.append(''.join(combo).title())

        random.shuffle(words)

        # Option 2: Avoid repeating passwords
        used_passwords = set()

        for word in words:
            random_component = random.choice(components)  # Select a random component for each word
            if any(char.isdigit() for char in word):  # Check if word contains a digit
                password = word + random_component
            else:
                password = word[::-1] + random_component
            if len(password) >= 6 and len(password) <= 14 and password not in used_passwords:
                used_passwords.add(password)
                if len(used_passwords) >= wordlist_length:
                    break

        wordlist.extend(used_passwords)

        attempts += 1

    approx_passwords = len(wordlist) * (max_attempts // attempts)

    # Option 4: Incorporate word transformations
    transformed_wordlist = []
    for password in wordlist:
        transformed_wordlist.append(password)
        transformed_wordlist.append(password[::-1])
        transformed_wordlist.append(password.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0'))

    # Option 5: Customization options
    random.shuffle(transformed_wordlist)
    wordlist = transformed_wordlist[:wordlist_length]

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
