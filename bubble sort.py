# bubble sort

def single_pass(index, lst):
    for i in range(index+1, len(lst)): # iterate for every item AFTER the current one
        if lst[index] > lst[i]: # if its bigger than the one next to it
            lst[index], lst[i] = lst[i], lst[index]# swap
    return lst
    
def bubble_sort(to_sort):
    for i in range(0, len(to_sort)): # iterate for every item
        to_sort = single_pass(i, to_sort) # do a pass
    return to_sort

# debugging stuff
import random
lst = [random.randint(0,1000) for _ in range(1000)]

print(bubble_sort(lst))
