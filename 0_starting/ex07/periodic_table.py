import sys

def create_html(dictionary):
	html = open('periodic_table.html', 'w')
	html.write('<!DOCTYPE html>\n')
	html.write('<html>\n')
	html.write('\t<head>\n')
	html.write('\t\t<title>Periodic Table</title>\n')
	html.write('\t</head>\n')
	html.write('\t<body>\n')
	html.write('\t\t<table>\n')
	html.write('\t\t\t<tr>\n')
	for key, values in dictionary.items():
		details_dict = dict(item.split(':') for item in values.split(', '))
		html.write('\t' * 4 + '<td style="border: 1px solid black; padding:10px">\n')
		html.write('\t' * 5 + '<h4>' + key + '</h4>\n')
		html.write('\t' * 6 + '<ul>\n')
		html.write('\t' * 7 + '<li>NO ' + details_dict["number"] + '</li>\n')
		html.write('\t' * 7 + '<li>' + details_dict["small"].strip() + '</li>\n')
		html.write('\t' * 7 + '<li>' + details_dict["molar"] + '</li>\n')
		html.write('\t' * 7 + '<li>' + details_dict["electron"] + ' electron</li>\n')
		html.write('\t' * 6 + '</ul>\n')
		html.write('\t' * 4 + '</td>\n')
	html.write('\t' * 3 + '</tr>\n')
	html.write('\t' * 2 + '</table>\n')
	html.write('\t</body>\n')
	html.write('</html>\n')

def run():
	# Read the file and parse the content into a dictionary
	elements_dict = {}
	with open('periodic_table.txt', 'r') as file:
		for line in file:
			key, value = line.split('=', 1)
			elements_dict[key.strip()] = value.strip()

	create_html(elements_dict)


if __name__ == '__main__':
	run()
