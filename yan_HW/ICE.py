from Resturant import restaurant

class IceCreamStand(restaurant):
    welcome_message = "WELCOME TO ICE CREAM STAND"
    #flavor = ["Mint"]

    def __init__(self, name, flavors):
        super().__init__(name, "icecream")
        self.flavors = flavors

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

    @staticmethod
    def print_welcome():
        print(IceCreamStand.welcome_message)

ice_cream_stand = IceCreamStand( "yan's ice", ["Mint","Apple","Chocolate"])
ice_cream_stand.show_flavors()
ice_cream_stand.add_flavor("Honey")
ice_cream_stand.show_flavors()
ice_cream_stand.print_welcome()

IceCreamStand.print_welcome()
print(ice_cream_stand.flavors)

print(ice_cream_stand.cuisine_type)
print(ice_cream_stand.restaurant_name)


list1 = ["apple", "bananna", "chocolate"]
for a in list1:
    print(a)
