import sys

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



if __name__ == '__main__':
	if (len(sys.argv) != 2):
		exit()
	run(sys.argv[1])
