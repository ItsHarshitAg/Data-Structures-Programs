def find_single_number(nums):
    if len(nums) == 1:
        return nums[0]
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if mid %2==1:
            mid -=1
        if nums[mid] != nums[mid + 1]:
            high = mid
        else:
            low = mid + 2
    return nums[low]
print(find_single_number([1,1,3,3,4,4,5,8,8])) #5