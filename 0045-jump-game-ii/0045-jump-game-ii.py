class Solution:
    def jump(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        cur_end, cur_far = 0,0
        for i in range(n-1):
            cur_far = max(cur_far, i+nums[i])
            if i == cur_end:
                result += 1
                cur_end=cur_far
        return result