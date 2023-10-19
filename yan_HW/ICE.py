from Resturant import restaurant

class IceCreamStand(restaurant):
    def __init__(self,restaurant_name , cuisine_type,flavor):
        super().__init__(restaurant_name, cuisine_type)
        self.flovar = flavor

    def my_ice_cream_flavors(self):
        for flavor in self.flovar:
            print(flavor)

ice_cream_stand=IceCreamStand( "yan's ice", "icecream" , ["Mint","Apple","Choco late"])
ice_cream_stand.my_ice_cream_flavors()
print(ice_cream_stand.cuisine_type)
print(ice_cream_stand.restaurant_name)