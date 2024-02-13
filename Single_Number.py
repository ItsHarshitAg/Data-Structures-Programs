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

"""
The `naive_` function takes an array as input and returns the index of the first element that occurs
only once in the array.

:param arr: The parameter "arr" is a list of numbers
:return: the index of the first element in the given array that is not repeated.
"""

def naive_(arr):
    for i in range(len(arr)):
        # keep the current element fixed
        is_single_num = 1
        # flag element is to check if we meet a double number 
        for j in range(len(arr)):
            # check for double number
            if i != j and arr[i] == arr[j]:

                is_single_num = 0
                break
        
        if is_single_num == 1:
            return i


"""
The function `searching_sorting` sorts an input array and returns the index of the first element
that is different from its adjacent elements.

:param arr: The parameter "arr" is a list of elements that you want to sort and search through
:return: the index of the first element in the sorted array that is not equal to its adjacent
elements.
"""
def searching_sorting(arr):
    arr.sort()
    for i in range(len(arr)):
        if i == 0:
            if arr[i] != arr[i+1]:
                return i
        
        elif i == len(arr) - 1:
            if arr[i] != arr[i - 1]:
                return i
        
        else:
            if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
                return i

"""
The `hashmap` function takes an array as input, creates a dictionary to store the frequency of each
element in the array, and returns the first element that appears only once.

:param arr: The parameter `arr` is a list of elements
:return: the key in the dictionary `ref_dict` that has a value of 1.
"""
def hashmap(arr):

    ref_dict = dict()
    for i in range(len(arr)):
        if arr[i] not in ref_dict:
            ref_dict[arr[i]] = 1
        else:
            ref_dict[arr[i]] += 1

    
    for key, value in ref_dict.items():
        if value == 1:
            return key