# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for i in s:
            # if it's a value
            if i not in dictionary:
                stack.append(i)
            elif not stack:
                return False
            else:
                curr = stack.pop()
                if dictionary.get(i) != curr:
                    return False
        return not stack

# Trace
# [  ]


        
