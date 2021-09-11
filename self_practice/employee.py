class Employee():
	"""Basic info about the employee"""
	
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary
	
	def give_raise(self, salary_raised=5000):
		self.salary += salary_raised
		return self.salary
		
