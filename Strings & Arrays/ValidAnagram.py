"""
Leetcode problem #242
Link: https://leetcode.com/problems/valid-anagram/submissions/1833768369/

We could create a hashmap which stores the count of each and 
compare the hashmaps.
have one hashmap where we go and add each letter, then remove the count
going through the nect string

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        for char in t:
            if char not in counts:
                return False
            elif counts[char] == 0:
                return False
            else:
                counts[char] -= 1
        for elt in counts:
            if counts[elt] != 0:
                return False
        return True
