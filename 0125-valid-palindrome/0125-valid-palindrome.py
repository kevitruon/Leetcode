class Solution:

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            while i<j and not s[l].isalnum():
                l+=1
            while i<j and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

    