import json

numbers = [v**3 for v in range(1, 11, 2)]
filename = 'numbers.json'

with open(filename, 'w') as f:
	json.dump(numbers, f)

with open(filename) as f:
	numbers = json.load(f)
print(numbers)