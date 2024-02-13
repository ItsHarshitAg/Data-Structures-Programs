def linear_search(lst,key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

print(linear_search([4,1,2,1,2], 1))
