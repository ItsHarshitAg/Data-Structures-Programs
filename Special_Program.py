# #formula = sn= (sn-1)+"0"+(sn-1)compliment
# #find the kth index at the nth string
# def compliment(st):
#     result = ""
#     for i in range(len(st)):
#         if st[i] == "0":
#             result += "1"
#         else:
#             result += "0"
#     return result


# def find_kth_index(s, k, n):
#     for i in range(n):
#         s = s + "0" + compliment(s)
#     print(s)
#     return s[k]




















# print(find_kth_index("0", 2, 2))
# # 0 001 0010110 001011001101001 0010110011010010110100110010110 001011001101001011010011001011001101001100101101001011001101001
# # what is the relationship between n and K
# # 2^0 = 1

# def flipbit(n):
#     return n ^ 1


# def find_kth_index(s,e,b,k ):
#     mid = s+e // 2
#     if k == mid:
#         return b
#     if k < mid:
#         return find_kth_index(s[:mid], k, n - 1,flipbit(b))
#     else:
#         return find_kth_index(s[mid:], k - mid, n - 1,b)
    
# start=0
# n=2
# k=3
# end=(2**n)-2
# b=0
# print(find_kth_index(start,end,b,k))

def flip(b):
    if b == 1:
        return 0
    else:
        return 1


def binary_search(start, end, k, bit):
    mid = (start + end) // 2
    # print(start, end, mid, bit, k)
    if mid == k:
        print(bit)
        return
    
    elif mid < k:
        start = mid + 1
        bit = flip(bit)
        binary_search(start, end, k, bit)
        
    else:
        end = mid - 1
        binary_search(start, end, k, bit)
        
    

n = 2
k = 3

start = 0
end = 2 ** (n + 1) - 2
print(f"len of string: {end + 1}\n\n")

binary_search(start, end, k, 0)