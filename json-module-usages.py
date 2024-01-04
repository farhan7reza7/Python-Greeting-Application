"""showing the uses of json module:
1. writing python data in json file in json format
2. reading json data from json file in python data format
"""

import json

# Create a list of cubes of odd numbers from 1 to 10
numbers = [v**3 for v in range(1, 11, 2)]

# Specify the filename for storing the list
filename = 'numbers.json'

# Open the file in write mode and dump the list into it
with open(filename, 'w') as f:
	json.dump(numbers, f)

# Open the file in read mode and load the list from it
with open(filename) as f:
	numbers = json.load(f)

# Print the loaded list
print(numbers)
