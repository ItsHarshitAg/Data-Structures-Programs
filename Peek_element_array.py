#find the peek element in the given array
#[6,13,7,-5,4,3,19]

def find_peek_element(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return nums[low]

print(find_peek_element([6,13,7,5,4,3,19])) #13




#linear search
def find_peek_element(nums):
    for i in range(len(nums)):
        if nums[i] > nums[i + 1]:
            return nums[i]
    return nums[len(nums) - 1]

print(find_peek_element([6,13,7,-5,4,3,19])) #13