"""Greet the user by their username.    
    If the username is stored in a file(file crerated using json moodule from the same/this program/script), it will ask the user to confirm identity.
    If not, it will prompt the user to create a new username.
"""

import json

def greet_user():
    """Greet the user by their username.    
    If the username is stored in a file, it will ask the user to confirm.
    If not, it will prompt the user to create a new username.
    """
    filename = 'username.json'
    username = get_stored_user(filename)
    if username:
        user = input(f"Are you {username}? Click y/n: ")
        if user == 'y':
            print(f"Welcome back, dear {username}!")
        else:
            username = create_new_user(filename)
            print(f"We'll remember you, dear {username}!")
    else:
        username = create_new_user(filename)
        print(f"We'll remember you, dear {username}!")

def get_stored_user(filename):	
    """Retrieve the stored username from a file.
    Args:
        filename (str): The name of the file where the username is stored.
    Returns:
        str: The stored username, or None if the file does not exist.
    """
    try:
        with open(filename) as f:
            username = json.load(f)
        return username	
    except FileNotFoundError:
        return None

def create_new_user(filename):	
    """Prompt the user to create a new username and store it in a file.
    Args:
        filename (str): The name of the file where the username will be stored.
    Returns:
        str: The new username.
    """
    username  = input("Write your username: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

greet_user()
