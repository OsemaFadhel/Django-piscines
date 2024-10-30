import sys

def search_state(state, states):
	for key, value in states.items():
		if (state.upper() == key.upper()):
			return value, key
	return (None)

def search_capital(capital, capital_cities):
	for key, value in capital_cities.items():
		if capital.capitalize() == value.capitalize():
			return key, value
	return None

def run(argv):
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

	input_list = [i.strip() for i in argv.split(',') if i.strip()]

	for i in input_list:
		result = search_state(i, states)
		if result:
			state_abbr, state_name = result
			print(f"{capital_cities[state_abbr]} is the capital of {state_name}")
		else:
			result = search_capital(i, capital_cities)
			if result:
				state_name, capital_value = result
				for key, value in states.items():
					if (state_name == value):
						print(f"{capital_value} is the capital of {key}")
						break
			else:
				print(f"{i} is neither a capital city nor a state")

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		exit()
	run(sys.argv[1])
