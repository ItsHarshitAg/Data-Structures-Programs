#find the next greater element greater that the target in a sorted array
def NextGreaterElement(arr, target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            result = mid
            start = mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    return arr[result]

print(NextGreaterElement([1,1,2,3,4,5,10,20,23,30,40],24))