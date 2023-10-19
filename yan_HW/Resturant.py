class restaurant:
    def __init__(self, restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        print (self.restaurant_name , self.cuisine_type)

    def open_restaurant(self):
        print ('we are open')

    def set_number_served(self, people):
        self.number_served = people
    
    def count_number_served(self):
        print("we served", str(self.number_served),"people today")
    
    def update_number_served(self,people):
        self.count_number_served = people
    
    def increment_number_served(self, more_people):
        self.number_served += more_people

my_restaurant = restaurant("3pig", "BBQ")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(100)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(10)
my_restaurant.count_number_served()
