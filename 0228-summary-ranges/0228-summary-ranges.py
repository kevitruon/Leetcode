class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: #if [] return []
            return nums

        start = nums[0]
        end = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i]-1 != nums[i-1]: #At start of new interval push previous interval to res.
                if start == end:
                    res.append(f'{start}')
                else:
                    res.append(f'{start}->{end}')
                start = nums[i]
                end = nums[i]
            else:
                end = nums[i]
        if start!=end:
            res.append(f'{start}->{end}')
        else:
            res.append(f'{start}')
        return res




