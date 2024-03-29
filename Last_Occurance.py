#Find the index position of the Last occurance of a target in a sorted array
def LastOccurance(arr, target):
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
            end = mid - 1
    return result

print(LastOccurance([1,1,2,2,3,4,5],2))