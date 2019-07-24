class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        res = ''
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in range(len(s)):
            if s[i] in vowels: stack.append(s[i])

        for char in s:
            if char in vowels:
                res = res + stack.pop()
            else:
                res = res + char
        return res

class Solution2:
    def reverseVowels(self, s: str) -> str:
        ptr1, ptr2 = 0, len(s) - 1
        res = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while ptr1 < ptr2:
            while ptr1 < ptr2 and s[ptr1] not in vowels:
                ptr1 += 1
            while ptr2 > ptr1 and s[ptr2] not in vowels:
                ptr2 -= 1
            if s[ptr1] in vowels and s[ptr2] in vowels:
                res[ptr1], res[ptr2] = res[ptr2], res[ptr1]
            ptr1 += 1
            ptr2 -= 1
            
        return ''.join(res)
