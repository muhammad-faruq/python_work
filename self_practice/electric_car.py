from car import Car

class Battery():
	"""A simple attempt to model a battery."""
	
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""Print a statement describing battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This car can go approximately " + str(range)
		message += " miles on full charge."
		print(message)
	
	def upgrade_battery(self):
		if self.battery_size == 70:
			self.battery_size = 85
			print("Battery size upgraded to 85-kWh")
		elif self.battery_size == 85:
			print("No further upgrades can be done to your battery!")


class ElectricCar(Car):
	"""It's like a car but its electric!"""
	def __init__(self, make, model, year):
		"""Initialize attributes of parent class.
		Then initiallizes the attributes to an electric car"""
		super().__init__(make, model, year)
		self.battery = Battery()

# ~ my_tesla = ElectricCar('tesla', 'model s', 2016)
# ~ print(my_tesla.get_descriptive_name())
# ~ my_tesla.battery.describe_battery()
# ~ my_tesla.battery.get_range()
