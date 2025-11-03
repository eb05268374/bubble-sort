# bubble sort

def single_pass(index, lst):
    for i in range(index+1, len(lst)):
        if lst[index] > lst[i]: # if its bigger than the one next to it
            temp = lst[i]
            lst[i] = lst[index]
            lst[index] = temp # swap
    return lst

def change_to_reference_index_and_score(array): # THIS IS UNFINISHED!!!!!!
    return array

def bubble_sort(to_sort):
    for i in range(0, len(to_sort)):
        to_sort = single_pass(i, to_sort)
    return to_sort

# debugging stuff
import random
lst = [random.randint(0,1000) for _ in range(1000)]

print(bubble_sort(lst))
