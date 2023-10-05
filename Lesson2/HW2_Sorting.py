import random
import time

TOTAL_NUMBER = 10

numbers1 = [*range(TOTAL_NUMBER)]
random.shuffle(numbers1)
numbers2 = numbers1.copy()
if TOTAL_NUMBER <= 50:
    print(numbers2)

def Swap(list,n,m):
    temp = list[n]
    list[n] = list[m]
    list[m] = temp

def BubbleSort(list):
    #TODO: write your sorting algorithm here.
    size = len(list)
    for i in range(size):
        for j in range(size-1,i,-1):
            if list[i] > list[j]:
                Swap(list,i,j)

def QuickSort(list):
    if len(list) <= 1:
        return list
    mid = list[len(list)//2]
    left = []
    right = []
    for n in list:
        if n < mid:
            left.append(n)
        elif n > mid:
            right.append(n)
    return QuickSort(left)+ [mid] + QuickSort(right)


st = time.time()
numbers1.sort()
et = time.time()
elapse_time = et - st
print("Official sorting algorithm cost " + str(elapse_time) + " seconds.") 

st = time.time()
numbers2 = QuickSort(numbers2)
et = time.time()
elapse_time = et - st
if TOTAL_NUMBER <= 50:
    print(numbers2)
print("Your sorting algorithm cost " + str(elapse_time) + " seconds.") 