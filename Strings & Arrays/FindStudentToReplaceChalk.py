# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

"""
U:
- Start with k pieces of chalk, which decreases by chalk[i] everytime student i 
is called to do a problem
- If k is every less than chalk[i], student i must replace the chalk. return i

Edge cases?
- What is the scope? 1, 10^5
    - We do need to be time sensitive

M: Array Problem
- Use dynamic programming and hashmaps to store values

P:
- While loop (true)
-inside the loop decrement k
- to help with large input we can store the total value summed from the first loop

1. initialize an i at 0
2. set n to len(chalk)
3. infinite while loop
4. check if i == n
    - if it is, reset i = 0
5. check if k is less than chalk[i]
    - if it is, return i
6. subtract chalk[i] from k


"""

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        # 1. initialize an i at 0
        # 2. set n to len(chalk)
        n = len(chalk)
        total = 0
        for i in range(0,n):
            # check if k is less than chalk[i]
            if k < chalk[i]:
                return i
            # subtract chalk[i] from k
            k -= chalk[i]
            total += chalk[i]

        k = k % total

        for i in range(0,n):
            # check if k is less than chalk[i]
            if k < chalk[i]:
                return i
            # subtract chalk[i] from k
            k -= chalk[i]
        
        return -1
        
"""
Trace:
chalk = [3,4,1,2]
k = 22
i = 0
n = 4
expected = 1
"""
