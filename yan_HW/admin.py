from user import User 

class Admin(User):
    def __init__(self, first_name , last_name, gender, years):
        super().__init__(first_name , last_name, gender, years)
        self.privileges = []

    def show_privileges(self):
        for privileges in self.privileges:
            print("admin privileges are" + ' '+ privileges)

SuperAdmin = Admin("lucas", "yan", "male", "25")
SuperAdmin.privileges = ["can add post","can delete post","can ban user"]
SuperAdmin.show_privileges()





