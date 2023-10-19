class User:
    def __init__(self, first_name , last_name, gender, years):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.years = years
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name, self.last_name)
        print(self.gender)
        print(self.years)

    def greet_user(self):
        print ('Welcome'+ self.first_name)

    def print_login_attempts(self):
        print ( "login attempts are" , str(self.login_attempts))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0 

user1 = User("Ruifeng","Yan","male", 25)

user1.describe_user()
user1.greet_user()

user1.login_attempts= (0)
user1.increment_login_attempts()
user1.print_login_attempts()

user1.reset_login_attempts()
user1.print_login_attempts()