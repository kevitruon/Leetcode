class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arrLen = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= arrLen:
                arrLen = i
        return arrLen == 0