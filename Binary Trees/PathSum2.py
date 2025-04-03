 # https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
U: 
- Can we assume binary tree? Yes
- Can we assume BST? No
- What is the node count range? [0, 5000]
- What is the node value range? [-1000, 1000]

M:
Any similar problems or approaches?
- similar to the root to leaf problem we just need to store 
values instead of simply returning
Traversal method?
- Probably pre order
Hashmap to store values?
- We could store the paths in a hashmap, but I don't think
that would be the best method
Recursive or iterative?
- Thinking of recursion
We may want to have a global variable for the final list
We may have a helper method that returns a list if it is 
true at the end

Tracing notes:
- We start at the root, if it's null return the list as is
- We can send the root to a helper method to make and test 
lists and paths
    - Check if the root is None
    - Subtract the val from the targetSum
    - add the val to a list
    - Check if the root is a leaf
        - If it is and targetSum == 0
            - append the list to the master list
            - return
        - If it is and targetSum != 0
            - return
    - call the method on left and right
- Return the masterList one the helper method has ran through the tree
"""
class Solution:
    def __init__(self):
        self.masterList = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    
        list = []
        self.helper(root, targetSum, list)

        return self.masterList

    def helper(self, root: Optional[TreeNode], targetSum: int, list: List[int]):
        if root is None:
            return
        targetSum -= root.val
        list.append(root.val)
        if root.left is None and root.right is None:
            if targetSum == 0:
                self.masterList.append(list.copy())
            list.pop()
            return

        self.helper(root.left, targetSum, list)
        self.helper(root.right, targetSum, list)
        list.pop()
    
# Trace
# Master List: [[5, 4, 11, 2]]
# targetSum: 0
# list: [5, 4, 11]
