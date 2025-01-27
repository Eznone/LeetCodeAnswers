class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 0
            else:
                dict[num] += 1
        
        for num, count in dict.items():
            if count > 0:
                return True
                
        return False