class Restaurant():
	"""A simple restaurant."""
	def __init__(self, restaurant_name, cuisine_type, number_served=0):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served
		
	def describe_restaurant(self):
		print("Welcome to " + self.restaurant_name.title() + " we serve "
			+ self.cuisine_type + " food.")
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is now open for business!")

	def set_number_served(self, served):
		self.number_served = served
		
	def increment_number_served(self, increment):
		self.number_served += increment
