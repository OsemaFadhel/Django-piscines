import requests, sys, json, dewiki

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: request_wikipedia.py '<search_term>'")
		sys.exit(1)

	file_name = sys.argv[1].replace(" ", "_")

	try:
		url = "https://en.wikipedia.org/w/api.php"
		params = {
			"action": "query",
			"format": "json",
			"page": file_name,
			"prop": "revisions",
			"rvprop": "content",
			"rvslots": "main",
			"titles": file_name,
			"redirects": 1
		}

		response = requests.get(url, params=params)
		response.raise_for_status()
		data = response.json()

		# Extract text from json
		page_id = data.get("query").get("pages")
		if page_id == "-1":
			raise Exception("Page not found!")

		page_content = None

		print(page_id)

		for key in page_id:
			if "revisions" in page_id[key]:
				page_content = page_id[key]["revisions"][0]["slots"]["main"]["*"]
				break

		if page_content is None:
			raise Exception("Page not found!")

		# Parse wiki text
		wiki_text = dewiki.from_string(page_content)


		# Save to file
		file_path = f"{file_name}.txt"
		with open(file_path, "w") as file:
			file.write(wiki_text)

		print(f"File {file_path} created successfully!")

	except Exception as e:
		print(e)
		sys.exit(1)
