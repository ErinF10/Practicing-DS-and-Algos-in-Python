# https://leetcode.com/problems/k-closest-points-to-origin/

"""
Understand:
- We are looking to find the k neared points to the origin

Edge cases:
- We have very large input so we need to be incredibly time and space conscious here
- We will now have an empty set
- k will not be larger than out array

Match: 2D Array/ Heap problem
- We wil most likely use a heap to solve this because we are looking for k nearest

Plan:
- We can use python's heapq to transform the array in place
- we can create a heap based on the disctances using the __lt__ function to override the classes comparison

"""
class Solution:
   
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(point1: List[int], point2: List[int] = [0,0]):    
            return math.sqrt(((point1[0] - point2[0]) ** 2) + (point1[1] - point2[0]) ** 2)

        sorted_points = sorted(points, key=euclidean_distance)
        return sorted_points[:k]
