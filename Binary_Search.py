def binary_search(arr, x):
    # first and last keep track of the search boundaries
    first = 0
    last = len(arr) - 1
    mid = 0
    while first <= last:
        mid = (last + first) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            first = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            last = mid - 1
        # x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

print(binary_search([2, 3, 4, 10, 40], 10))
print(binary_search([2, 3, 4, 10, 40], 2)) 