class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        countD = defaultdict(int) #key:count
        idx = 0
        for i in range(len(nums)):
            if countD.get(nums[i],0)<2:
                countD[nums[i]] += 1
                nums[idx]=nums[i]
                idx+=1
        return idx
