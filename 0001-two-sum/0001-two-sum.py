class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numdict = {}

        for i, num in enumerate(nums):
            value = target - num
            if value not in numdict.keys():
                numdict[num] = i
            else:
                return [numdict[value], i]
