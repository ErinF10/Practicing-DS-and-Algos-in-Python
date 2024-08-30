# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree. (Leetcode problem 108)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        mid = len(nums) // 2
        newNode = TreeNode(nums[mid])

        newNode.left = self.sortedArrayToBST(nums[0:mid])
        newNode.right = self.sortedArrayToBST(nums[mid + 1:len(nums)])

        return newNode
        
