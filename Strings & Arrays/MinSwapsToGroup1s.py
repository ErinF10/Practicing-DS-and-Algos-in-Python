# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

"""
U:
Can we have an empty array? No

M: Array Problem
What tools/methods can we use?
- Hashmap to store data/add an indicator within the array
- Two-pointer method
- Sorting the array
- Pre computation
    - Suffix sum
- Sliding window technique
- Traversing the array multiple times

- We can use suffix and sliding window to approach this problem
# Suffix sum:
#                 i   j
#         arr: [1,3,4,1,2]
#                 i -   j+1
# suffix sum: [11,10,7,3,2]
# - Create a new array of the same and create an array with the sums going
# in opposite order of prefix sum.
Sliding window:
- Two pointers that move at the same speed for a set length
- We could find the number of 1's, and do a window of that length

Test case trace:
[0,1,1,1,0,0,1,1,0] -> 2
   ^       ^       
[0,1,1,1,0,1,0,1,0] -> 1

P:
#Sliding window

1. Traverse through array to find number of 1's (variable total to store this)
2. Initialize sliding window at arr[i] and arr[j]
    - Where i = 0, and j = total - 1
    - variable mostSoFar to keep track
3. Count the number of zeroes within the sliding window
    - First one, we just go through and count
4. subtract arr[i -1] and add arr[j]
5. Update mostSoFar

int j = total - 1
for (int i = 0; i < arr.length; i++) {
    do stuff
    j = (j + 1) % arr.length
}


"""

class Solution:
    def minSwaps(self, arr: List[int]) -> int:
        total = 0
        for elt in arr:
            total += elt
        i, j, maxSoFar = 0, total - 1, 0
        for k in range(total):
            maxSoFar += arr[k]
        currMax = maxSoFar
        while i < len(arr):
            currMax -= arr[i]
            i += 1
            if j == len(arr) - 1:
                j = 0
            else:
                j += 1
            currMax += arr[j]
            if currMax > maxSoFar:
                maxSoFar = currMax

        return total - maxSoFar

"""
[0,1,0,1,1,0,0] -> 1
   j         i   
total: 3
maxSoFar: 2
currMax: 1

"""
