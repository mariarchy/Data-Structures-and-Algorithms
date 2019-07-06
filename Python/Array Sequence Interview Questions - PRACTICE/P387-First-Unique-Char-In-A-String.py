# s = "leetcode"
# s = "level"
# s = "raceecar"
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for index, char in enumerate(s):
            if char not in d:
                d[char] = index
            else:
                d[char] = -1
        for char in s:
            if d[char] != -1:
                return d[char]
        return -1
