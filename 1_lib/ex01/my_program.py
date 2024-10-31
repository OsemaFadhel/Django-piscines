from local_lib import path

if __name__ == '__main__':
	try:
		dir_path = path.Path("new_dir")
		file_path = dir_path / "new_file.txt"

		dir_path.mkdir()
		file_path.touch()
		print(file_path.exists())

		#write to file
		file_path.write_text("Hello, World!")
		print(file_path.read_text())

	except Exception as e:
		print(e)
