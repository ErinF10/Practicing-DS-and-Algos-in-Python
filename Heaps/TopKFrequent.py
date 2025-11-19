"""
Leetcode problem #347
Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/1833769627/

Plan: Array
- Because we are finding the k most frequent, it seems as though heaps
will be the most fitting here

Idea 1: Hash map
1. Put the elt counts into a hash map (O(n))
2. Heapify the hashmap values using heapq (O(n))
3. Get top k values and key pairs and add to a list as you go (O(k*n))
Final Time complexity: (O(3*k*n))
Final space complexity: (O(n))




"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Put the elt counts into a hash map (O(n))
        val_counts = defaultdict(int)
        for num in nums:
            val_counts[num] += 1
        
        # 2. Heapify the hashmap values using heapq (O(n))
        max_heap = []
        for value in val_counts.values():
            max_heap.append(-value)

        heapq.heapify(max_heap)

        # 3. Get top k values and key pairs and add to a list as you go (O(k*n))
        top_k = []
        while k > 0:
            popped = -(heapq.heappop(max_heap))
            for key, val in val_counts.items():
                if val == popped:
                    next_key = key
                    val_counts[key] = 0
                    break
            top_k.append(next_key)
            k -= 1

        return top_k
