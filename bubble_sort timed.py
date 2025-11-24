import random, time

items = [random.randint(0,1000) for _ in range(0,10000)] # make a big list of random numbers
n = len(items)
swap = True

start = time.time()
while swap:
    swap = False
    for index in range(0, n-1):
        if (items[index] > items[index+1]): # swap index and index + 1 if index is greater
            temp = items[index] # -- swaps index and index + 1
            items[index] = items[index+1]
            items[index+1] = temp # end swap code --
            swap = True

end = time.time()

speed = round(end-start, 5)

print(f"Time taken is {speed}")

# as the N^2 would suggest, the time the algorithim takes dramatically increases as you increase the size of the list
