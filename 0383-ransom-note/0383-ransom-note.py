class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mCount = defaultdict(int)
        rCount = defaultdict()

        for s in magazine:
            mCount[s] = 1 + mCount.get(s,0)

        for s in ransomNote:
            if mCount[s] <= 0:
                return False
            mCount[s] = mCount.get(s) - 1
        return True