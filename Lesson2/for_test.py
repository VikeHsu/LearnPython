cars = ['audi', 'bmw', 'subaru', 'toyota']

# for list
count = 1
for car in cars:
    print(count)
    count += 1
    print(car.title())

r = [1,2,3,4,5,6]
count =1
for i in range(6):
    print(count)
    count += 1
    print("i:"+ str(i))


for car in cars:
    if car == 'honda':
        print("found Honda!")
        break