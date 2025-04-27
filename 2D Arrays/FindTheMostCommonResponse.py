"""
We can loop through each, removing duplicates and counting as we go, ensuring that we dont count duplicates
- Use a hashmap to store the data, map that stores maps?

responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
mostCommon = {}
for arr in responses:
    responseCount = {}
    for response in arr:
"""

class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        uniqueResponses = []
        for arr in responses:
            uniqueArr = set()
            for response in arr:
                uniqueArr.add(response)
            uniqueResponses.append(uniqueArr)
            
        mostCommon = {}
        for arr in uniqueResponses:
            for response in arr:
                if response not in mostCommon:
                    mostCommon[response] = 1
                else:
                    mostCommon[response] += 1
        maxSoFar = mostCommon.keys()[0]
        for response in mostCommon.keys():
            if mostCommon[response] > mostCommon[maxSoFar]:
                maxSoFar = response
            if mostCommon[response] == mostCommon[maxSoFar]:
                if response < maxSoFar:
                    maxSoFar = response
        return maxSoFar
            
            
