def my_print():
	nb_file = open('numbers.txt', 'r')
	spl = nb_file.read().split(',')
	for i in spl:
		print(i) #.strip())
	nb_file.close()

if __name__ == '__main__':
	my_print()
