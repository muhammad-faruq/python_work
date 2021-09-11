class User():
	def __init__(self, first_name, last_name, login_attempts=0):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name
		self.login_attempts = login_attempts
		
	def describe_user(self):
		print("First name: " + self.first_name.title())
		print("Last name: " + self.last_name.title())
		print("Full name: " + self.full_name.title())
	
	def greet_user(self):
		print("Hello " + self.full_name.title() + "!")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
	def call_login_attempts(self):
		print("\n" + self.full_name.title() + " have attempted to log in " 
			+ str(self.login_attempts) + " times.")


class Privileges():
	def __init__(self, privileges):
		self.privileges = privileges
	
	def call_privileges(self):
		print("These are the privileges you have: ")
		for privilege in self.privileges:
			print("- " + privilege)

class Admin(User):
	"""Admin is a SuperUser"""
	
	def __init__(self, first_name, last_name, privileges, login_attempts=0):
		super().__init__(first_name, last_name, login_attempts=0)
		self.privilege = Privileges(privileges)
