class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx]=nums[i]
                idx+=1
        return idx
