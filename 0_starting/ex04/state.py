import sys

def search_capital(capital, capital_cities):
	for key, value in capital_cities.items():
		if (capital == value):
			return (key)
	return (None)

def run(capital):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
		}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
		}

	ret_value = search_capital(capital, capital_cities)

	if (ret_value == None):
		print("Unknown capital city")
	else:
		for key, value in states.items():
			if (ret_value == value):
				print(key)
				break


if __name__ == '__main__':
	if (len(sys.argv) != 2):
		exit()
	run(sys.argv[1])
