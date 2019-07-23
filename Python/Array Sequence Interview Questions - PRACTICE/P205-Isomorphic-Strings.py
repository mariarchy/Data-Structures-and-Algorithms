from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_map = {}
        t_map = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in s_map:
                if t_map[t[i]] == 0:
                    s_map[s[i]] = t[i]
                    t_map[t[i]] = 1
                else:
                    return False
            elif s_map[s[i]] != t[i]:
                return False
        return True

class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_dict, t_dict = {}, {}
        for i, val in enumerate(s):
            s_dict[val] = s_dict.get(val, []) + [i]
        for i, val in enumerate(t):
            t_dict[val] = t_dict.get(val, []) + [i]

        return sorted(s_dict.values()) == sorted(t_dict.values())
