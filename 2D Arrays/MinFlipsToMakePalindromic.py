# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

"""
U:
- Can we have a large input? Yes
- Can we have null input? No

M: 2D array problem
- Similar to the palindrome problem where you are allowed to flip bits
- Do we want to go through this iteratively or recursively?
- We can look at minimum needed for rows and then columns, and then compare the two
    - This should be O(2n*m)
How to find miniumum flips for rows:
1. Use regular isPalindrome method for each row, but when a discrepency is found you just need to increase flip count

How to find minimum flips for columns:
1. Create an array out of each column, and run it through the same method
Need to decrease space complexity:
call an isPalindrome method directly on grid but using indices

for each row:#labeled with i



"""

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        minFlipsRow = 0
        for arr in grid:
            count = 0
            for i in range(len(arr) // 2):
                if arr[i] != arr[len(arr) - 1 - i]:
                    count += 1
            minFlipsRow += count
            
        minFlipsCol = 0
        for j in range(len(grid[0])):
            count = 0
            top = 0
            bottom = len(grid) - 1
            while bottom - top > 0:
                if grid[top][j] != grid[bottom][j]:
                    count += 1
                top += 1 
                bottom -= 1
            minFlipsCol += count
        
        return min(minFlipsRow, minFlipsCol)
    
    # def countRowFlips(self, arr: List[int], count: int) -> int: 
    #         if len(arr) == 1 or len(arr) == 0:
    #             return count # 0 flips needed at base case
    #         if arr[0] != arr[len(arr) - 1]:
    #             count += 1
    #         return self.countRowFlips(arr[1:len(arr) - 1], count)
    
#     def countColFlips(self, grid: List[List[int]], count: int, top: int, bottom: int, j: int) -> int:
#         if bottom - top < 1: # we are at the middle
#             return count
#         if grid[top][j] != grid[bottom][j]:
#             count += 1
#         return self.countColFlips(grid, count, top + 1, bottom - 1, j)
    
    
        """
        Trace: [[0,1],
                [1,1]]
        j = 0
        minFlipsCol = 0
        
        countColFlips(grid, count=0, top=0, bottom=1, j=0)
        
        
        """
        
        
       
            
        
