"""
Leetcode problem #102

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U: 
M: Level order means we want to put a queue for each level
P:
- Use a queue to keep track of where we are in the tree
put 3 into the queue
take out 3 and put it into the array

put 9 into the queue put 20 into the queue (put 3's children into the queue)
pop the queue and put 9 into the array, then put 9's children into the queue
pop the queue and put 20 into the array, then put 20's children into the queue

pop the array, pop the array

Once the q is empty we are done

"""
class Solution:
  
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        q = []
        level = 0
        list = []

        if root is None:
            return arr
        
        q.append(root)

        while q:
            level = len(q)
            while level > 0:
                curr = q.pop(0)
                list.append(curr.val)
                if curr.left:
                    # print(root.left.val)
                    q.append(curr.left)
                if curr.right:
                    # print(root.right.val)
                    q.append(curr.right)
                level -= 1
            arr.append(list)
            list = []
            

        return arr

"""
Trace Notes:
q = []
curr = 7
level = 1
list = [15, 7]
arr = [[3], [9, 20], [15, 7]]
"""
        
