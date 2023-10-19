class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        for privileges in self.privileges:
            print("admin privileges are" + ' '+ privileges)

class Admin:
    def __init__(self,first_name , last_name, gender, years):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.years = years
        self.privileges = Privileges()
    

admin1 = Admin("lucas", "yan", "male", "25")

admin1.privileges.show_privileges()