TODO = """ maybe check again to fix, but logix is correct """

import sys, requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: python3 roads_to_philosophy.py <term>')
		sys.exit(1)

	term = sys.argv[1].replace(" ", "_")

	visited = []
	try:
		while True:
			url = f"https://en.wikipedia.org/wiki/{term}"
			response = requests.get(url)
			response.raise_for_status()

			soup = BeautifulSoup(response.text, 'html.parser')

			for link in soup.find_all('a'):
				if link.get('href').startswith('/wiki/') and ':' not in link.get('href') and 'Main_Page' not in link.get('href'):
					if link.get('href').split('/')[-1] not in visited:
						term = link.get('href').split('/')[-1]
						break

			if term in visited:
				raise Exception("It leads to an infinite loop !")
			visited.append(term)
			print(term)

			if term == "Philosophy":
				print(f"{len(visited)} roads from {sys.argv[1]} to Philosophy !")
				break


	except Exception as e:
		print(f"It leads to a dead end !")
		sys.exit(1)
	except requests.exceptions.HTTPError as e:
		print(f"HTTP Error: {e}")
		sys.exit(1)
