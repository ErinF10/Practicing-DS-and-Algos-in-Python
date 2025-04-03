# https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/1595124611/

  # Your function validPath is called as such:
# edges = [[0,1],[1,2],[2,0]]
# validPath(3, edges, 0 ,2)

"""
U:
Scope? At least one node
  - Fairly large input potential, need to be mindful of time
Edge Case:
- The graph may not be all together

M: Graph Problem
- Traversal method that will help us? BFS or DFS
- Add an array or hashmap for keeping track of seen edges

P:
- Put edges into an adjacency list
- Start with our source node
- From there we can use a BFS 
  - Stop when destination is found
  - Stop when we have already visited each connecting node

BFS:
- Use a queue to implement BFS iteratively
- Use recursion

Input: n = 3, edges = [ [0,1],[1,2],[2,0] ], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

edges = [ [0,1],[1,2],[2,0] ]
adjacencyList = {
  0: [1,2],
  1: [0,2],
  2: [1,0]
}

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
adjacencyList = {
  0: [1,2],
  1: [0],
  2: [0],
  3: [5,4],
  5: [3,4],
  4: [5,3]
}
visited = [0,1,2]
queue = []
"""
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        adjacencyList = defaultdict(list)
        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])

        queue = deque()
        queue.append(source)
        visited = set()

        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for elt in adjacencyList[curr]:
                if elt not in visited:
                    visited.add(elt)
                    queue.append(elt)
                    
        return False

    """
        edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
        adjacencyList = {
            0: [1,2],
            1: [0],
            2: [0],
            3: [5,4],
            5: [3,4],
            4: [5,3]
        }
        visited = [0]
        queue = [2]
        curr = 1
    """
        
    
