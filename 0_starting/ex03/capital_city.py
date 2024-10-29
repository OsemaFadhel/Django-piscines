import sys

def search_state(state, states):
	for key, value in states.items():
		if (state == key):
			return (value)
	return (None)

def run(state):
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

	ret_value = search_state(state, states)

	if (ret_value == None):
		print("Unknown state")
	else:
		print(capital_cities[ret_value])


if __name__ == '__main__':
	if (len(sys.argv) != 2):
		exit()
	run(sys.argv[1])
