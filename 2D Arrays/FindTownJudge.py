# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        graph = [0 for _ in range(n+1)]
        for edge in trust:
            graph[edge[0]]-=1
            graph[edge[1]]+=1

        for i in range(n+1):
            if graph[i] == n-1:
                return i
        return -1
