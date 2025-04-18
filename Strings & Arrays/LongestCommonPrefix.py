# https://leetcode.com/problems/longest-common-prefix/

"""
Input: strs = ["flower","flow","flight"]
Output: "fl"

output = []
while i (has next):
    char = strs[0][i]
    for string in strs:
        if string[i] != char:
            break out of while loop
    output.append(strs[0][i])

return output

i = 2
set = [o]
output = [f, l]
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = []
        minLength = len(strs[0])
        for string in strs:
            if len(string) < minLength:
                minLength = len(string)
        
        for i in range (0, minLength):
            setBreak = False
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    setBreak = True
                    break
            if setBreak:
                break
            output.append(strs[0][i])

        return "".join(output)

"""
Input: strs = ["flower","flow","flight"]
output = [f, l ]
i = 2
minLength = 4
char = o
setBreak =
"""
