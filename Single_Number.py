# # Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# # You must implement a solution with a linear runtime complexity and use only constant extra space.
# # Using XOR operator, we can solve this problem in O(n) time and O(1) space
# # XOR of a number with itself is 0. So, if we XOR all the elements of the array, we will be left with the single number
# # which is the non-repeating number.
    

def singleNumber(nums) -> int:
    result=0
    for i in nums:
        result ^= i
    return result
    
# singleNumber([4,1,2,1,2])

