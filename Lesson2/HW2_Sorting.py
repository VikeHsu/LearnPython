import random
import time

TOTAL_NUMBER = 10000

numbers1 = [*range(TOTAL_NUMBER)]
random.shuffle(numbers1)
numbers2 = numbers1.copy()
if TOTAL_NUMBER <= 50:
    print(numbers2)

def swap(list,n,m):
    temp = list[n]
    list[n] = list[m]
    list[m] = temp

def your_sort(list):
    #TODO: write your sorting algorithm here.
    print(list)

st = time.time()
numbers1.sort()
et = time.time()
elapse_time = et - st
print("Official sorting algorithm cost " + str(elapse_time) + " seconds.") 

st = time.time()
your_sort(numbers2)
et = time.time()
elapse_time = et - st
if TOTAL_NUMBER <= 50:
    print(numbers2)
print("Your sorting algorithm cost " + str(elapse_time) + " seconds.") 