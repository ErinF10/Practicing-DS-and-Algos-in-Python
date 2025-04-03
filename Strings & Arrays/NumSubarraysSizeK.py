"""
Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.
"""


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c = 0
        currSum = 0
        currSum = sum(arr[0:k])
        if currSum / k >= threshold:
            c += 1
        for i, x in enumerate(arr):
            if i == len(arr) - (k): break 
            currSum -= arr[i]
            currSum += arr[i + k]
            if currSum / k >= threshold:
                c += 1
        return c
      
