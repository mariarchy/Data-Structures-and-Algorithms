class Solution:
    def lengthOfLongestSubstring_Naive(self, s: str) -> int:
        if not s: return 0

        char_tracker = [0] * 26
        max_count = 0
        count = 0
        for i in range(len(s)):
            for j in range(0, len(s) - i):
                # if a duplicate is found, reset all values and update max (if needed)
                if char_tracker[ord(s[i + j]) - 'a'] or i == len(s) - i - 1:
                    max_count = max(max_count, j - i)
                    char_tracker = [0] * 26
                    count = 0
                    break
                else:
                    char_tracker[ord(s[i + j]) - 'a'] = 1

        return max_count

    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': return 0

        i = 0
        j = 1
        char_tracker = set(s[i])
        max_count = 1

        while i < len(s) and j <= len(s):
            if j == len(s) or s[j] in char_tracker:
                max_count = max(max_count, j - i)
                char_tracker.remove(s[i])
                i += 1
            else:
                char_tracker.add(s[j])
                j += 1

        return max_count
