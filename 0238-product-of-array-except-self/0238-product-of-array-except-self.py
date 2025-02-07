class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array_size = len(nums)
        answer = [1] * array_size

        product = 1
        for i in range(array_size):
            answer[i] = product
            product *= nums[i]

        product = 1
        for i in range(array_size - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer
