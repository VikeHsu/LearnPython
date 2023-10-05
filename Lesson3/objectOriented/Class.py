from Civic import civic
from Car import car

mycar = car("Honda", "Accord") #创建了一个类别为car的实例/对象 并给这个实例/对象命名为 mycar
print(mycar.make)
print(mycar.model)
print(mycar.milage)
mycar.drive(43000)
print(mycar.milage)

yourcar = car("Toyota", "Camry") #创建了另一个类别为car的实例/对象 并给这个实例/对象命名为 yourcar
print(yourcar.milage)
yourcar.drive(200)
print(yourcar.milage)

somecar = car() #创建了另一个类别为car的实例/对象 并给这个实例/对象命名为 somecar
print(somecar.get_make())
somecar.set_make("Ford")
somecar.set_model("F-150")
print(somecar.get_make())
print(somecar.get_model())

my_new_car = civic('Blue') #创建了一个类别为civic的实例/对象 并给这个实例/对象命名为 my_new_car
my_new_car.print()
my_new_car.drive(100)
print(my_new_car.milage)