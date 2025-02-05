from heapq import heappush, heappop, heapify
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numDict = {}

        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1

        # Negative values to simulate max heap
        # Since the heapify python function is normally min heap
        heap = [[-val, -key] for key, val in numDict.items()]
        heapify(heap)
        result = []
        for _ in range(k):
            result.append(-heappop(heap)[1])

        return result
        
