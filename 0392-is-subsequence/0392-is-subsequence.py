class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen, tLen = len(s),len(t)
        sPointer = tPointer = 0 
        if sLen == 0:
            return True
        while sPointer < sLen and tPointer < tLen:
            if s[sPointer]==t[tPointer]:
                sPointer+=1
            tPointer+=1
        return sPointer == sLen
                    
