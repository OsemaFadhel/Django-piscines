def my_var():
	my_var = 42
	print(my_var, "has a type ", type(my_var))
	my_var = "42"
	print(my_var, "has a type ", type(my_var))
	my_var = "quarante-deux"
	print(my_var, "has a type ", type(my_var))
	my_var = 42.0
	print(my_var, "has a type ", type(my_var))
	my_var = True
	print(my_var, "has a type ", type(my_var))
	my_var = [42]
	print(my_var, "has a type ", type(my_var))
	my_var = {42:42}
	print(my_var, "has a type ", type(my_var))
	my_var = (42,)
	print(my_var, "has a type ", type(my_var))
	my_var = set()
	print(my_var, "has a type ", type(my_var))

if __name__ == '__main__':
	my_var()
