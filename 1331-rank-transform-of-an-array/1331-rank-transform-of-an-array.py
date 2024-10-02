class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {} #value:rank
        sorted_unique_numbers = sorted(list(set(arr)))
        res = []

        for i in range(len(sorted_unique_numbers)):
            value_to_rank[sorted_unique_numbers[i]] = i+1

        for num in arr:
            res.append(value_to_rank[num])
        
        return res

