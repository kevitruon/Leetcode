class Solution:
    def maxArea(self, height: List[int]) -> int:
        greatestArea = 0
        l,r = 0, len(height)-1
        while l<r:
            currArea = min(height[l],height[r])*(r-l)
            greatestArea = max(greatestArea, currArea)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return greatestArea