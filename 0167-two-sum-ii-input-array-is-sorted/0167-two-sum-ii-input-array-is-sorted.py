class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l<r:
            summ = numbers[l]+numbers[r]
            if summ > target and l<r:
                r-=1
            elif summ < target and l<r:
                l+=1
            else:
                return [l+1,r+1]
        