import json

def greet_user():
	"""greet user."""
	filename = 'username.json'
	username = get_stored_user(filename)
	if username:
		user = input(f"Are you {username}?click y/n: ")
		if user == 'y':
		    print(f"welcome back, dear {username}!")
		else:
			username = create_new_user(filename)
			print(f"will remember you dear {username}!")
	else:
		username = create_new_user(filename)
		print(f"will remember you dear {username}!")


def get_stored_user(filename):	
	try:
		with open(filename) as f:
			username = json.load(f)
		return username	
	except FileNotFoundError:
		None

def create_new_user(filename):	
	username  = input("write youor username: ")
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

greet_user()
