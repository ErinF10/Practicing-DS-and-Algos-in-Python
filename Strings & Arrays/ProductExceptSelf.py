"""
Leetcode problem #238 
Link: https://leetcode.com/problems/product-of-array-except-self/

Output[i] is the product of all other elements except nums[i]

Brute force:
go through and multiply each other element (Takes O(n^2) time)

Plan: Array problem
- Hashmap
- Sliding window/Two-pointer
- Dynmaic pogramming

Ideas:
1. Find the full product, and divide the current number each time
Edge case: when there is only one zero
    - take the product besides the zero, that is the number for output[0], each 
    other number in output will be zero
Edge case: When there are two or more zeros
    - Each item in output will be zero

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        found_zero = False
        zero_location = 0
        for i, num in enumerate(nums):
            if found_zero and num == 0:
                return [0] * len(nums)
            if not found_zero and num == 0:
                found_zero = True
                zero_location = i
            else:
                product *= num
        if found_zero:
            output = [0] * len(nums)
            output[zero_location] = product
            return output
        output = []
        for num in nums:
            output.append(product // num)
        return output


        
