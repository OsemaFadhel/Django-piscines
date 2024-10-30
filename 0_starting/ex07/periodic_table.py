import sys

def create_html(dictionary):
	html = """
	<!DOCTYPE html>
	<html>
		<head>
			<title>Periodic Table</title>
			<style>
				h4 {{
					text-align: center;
				}}
			</style>
		</head>
		<body>
			<h1 style="display: flex; justify-content: center; color: blue; font-family: Arial;">Periodic Table</h1>
			<table>
				{templ}
			</table>
		</body>
	</html>
	"""

	template = """
					<td style="border: 2px solid black; padding:10px; background-color: #f0f0f0;">
						<h4>{key}</h4>
							<ul>
								<li>NO {number}</li>
								<li>{small}</li>
								<li>{molar}</li>
								<li>{electrons} electron</li>
							</ul>
					</td>
	"""

	# Create the HTML file
	templ = "<tr>"
	position = 0

	for key, values in dictionary.items():
		details_dict = dict(item.split(':') for item in values.split(', '))
		if position > int(details_dict["position"]):
			templ += "			</tr>\n				<tr>"
			position = 0
		for _ in range(position, int(details_dict["position"]) - 1):
			templ += "					<td></td>\n"
		position = int(details_dict["position"])
		templ += template.format(
			key=key,
			number=details_dict["number"],
			small=details_dict["small"],
			molar=details_dict["molar"],
			electrons=details_dict["electron"],
			)

	templ += "    </tr>\n"
	with open('periodic_table.html', 'w') as html_file:
		html_file.write(html.format(templ=templ))


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
