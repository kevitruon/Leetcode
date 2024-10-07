class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strings = s.split(" ")
        if len(pattern) != len(strings):
            return False
        if len(set(pattern)) !=len(set(strings)):
            return False
        hashmap = defaultdict(str) #char:string
        for i in range(len(pattern)):
            if hashmap.get(pattern[i], "") and hashmap[pattern[i]] != strings[i]:
                return False
            hashmap[pattern[i]] = strings[i]
        return True
