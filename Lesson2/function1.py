import random
import time
numbers = [*range(10000)]
random.shuffle(numbers)

def swap(list,n,m):
    temp = list[n]
    list[n] = list[m]
    list[m] = temp

def sort(list):
    while 1:
        swap(list,1,2)


#print(numbers)

st = time.time()
#sort(numbers)
numbers.sort()
et = time.time()
elapse_time = et - st
#print(numbers)
print(elapse_time)


def display_message():
    print('This is display message!')

def favorit_book(page, title='alice', author = "xxx"):
    print('One of my favorite books is '+ title + ' at page ' + str(page))
    print('Author is '+ author)
    result = 'No Error'
    if page <= 0 :
        result = "Error" 
    total_len = len(title) + len(author)
    return [result, total_len]


display_message()
favorit_book(10)
favorit_book(20, "Three body")
[x, y]=favorit_book(5, author='yyy')
print(x)
print(y)
[x, y]=favorit_book(-100, author='yyy')
print(x)
print(y)

x = ''

def city_country(city, country):
    global x
    x = "welcome to " + city + ", " + country
    #return x

city_country('Shanghai', 'China')
print(x)

'''
for num in numbers:
    print(num)
    print("*******")

print('*******************************')
numbers.sort()

for num in numbers:
    print(num)
    print("*******")

# custom print: 
for num in numbers:
    print(num)
    print("*******" )

'''