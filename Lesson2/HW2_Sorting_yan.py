import random
import time

TOTAL_NUMBER = 100

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
    if len(list) <= 1:
        return list
    left = []
    right = []
    piv = []
    pivot = random.choice(list)
    for val in list:
        if val == pivot:
            piv.append(val)
        elif val < pivot:
            left.append(val)
        else:
            right.append(val)
    return your_sort(left) + piv + your_sort(right )



    print(list)

def your_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0] 
        less = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]
        return your_sort(less) + [pivot] + your_sort(greater)
    print(list)


def your_sort(list):
    if len(list)<=1:
        return list
    
    mid = len(list) // 2 
    left_half = list[:mid]
    right_half = list[mid:]

    left_half = your_sort(left_half)
    right_half = your_sort(right_half)

    merged_arr = merge(left_half, right_half)
    return merged_arr

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

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