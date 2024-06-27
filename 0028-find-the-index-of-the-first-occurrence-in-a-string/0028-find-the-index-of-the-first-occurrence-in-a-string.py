class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==needle:
            return 0
        length = len(needle)
        for i in range(0,len(haystack),1):
            if haystack[i:i+length] == needle:
                return i
        return -1