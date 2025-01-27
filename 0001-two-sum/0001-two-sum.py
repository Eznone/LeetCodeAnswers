class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numMap = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in numMap:
                return [i, numMap[remainder]]
            numMap[num] = i
            