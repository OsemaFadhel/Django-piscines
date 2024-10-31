import antigravity
import sys

def check_date(date):
	try:
		year, month, day = date.split('-')
		if (len(year) != 4 or len(month) != 2 or len(day) != 2):
			raise ValueError("Invalid date format")
		return date
	except ValueError as e:
		print("An error occurred: ", e)
		exit()

def run(argv):
	latitude = float(argv[1])
	longitude = float(argv[2])
	date = check_date(argv[3])
	dow_open = float(argv[4])

	#date-dow format: 'YYYY-MM-DD-dow'
	full_date = date + '-' + str(dow_open)

	antigravity.geohash(latitude, longitude, full_date.encode())


if __name__ == '__main__':
	if (len(sys.argv) != 5):
		print("Usage: python geohashing.py <latitude> <longitude> <date Dow 'YYYY-MM-DD'> <Dow open>")
		exit()

	argv = sys.argv
	try:
		run(argv)
	except Exception as e:
		print("An error occurred: ", e)
		exit()
