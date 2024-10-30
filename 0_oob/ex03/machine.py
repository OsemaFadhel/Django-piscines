import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeMachine:
	def __init__(self):
		self.count = 0

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def repair(self):
		self.count = 0
		print("Machine repaired.")

	def serve(self, beverage):
		if self.count == 10:
			raise self.BrokenMachineException()

		drink = beverage() if random.randint(0, 1) == 0 else self.EmptyCup()

		self.count += 1

		return drink



if __name__ == '__main__':

	machine = CoffeMachine()
	drinks = [Coffee, Tea, Chocolate, Cappuccino]

	for i in range(25):
		try:
			print(machine.serve(random.choice(drinks)))
		except machine.BrokenMachineException as e:
			print(e)
			machine.repair()
		except Exception as e:
			print(e)
			break
		print()
