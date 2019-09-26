import unittest
def longestAlphabeticalString(s):
    if not s: return s
    end, max_len, curr_len, i = 0, 0, 1, 1
    while i < len(s):
        if ord(s[i]) >= ord(s[i-1]): curr_len += 1
        elif max_len < curr_len:
            end, max_len = i-1, curr_len
            curr_len = 1
        i += 1

    return s[end-max_len+1:end+1]

class Test(unittest.TestCase):
    def test_longest_alphabetical_substring(self):
        self.assertEqual(longestAlphabeticalString('abfcj'), 'abf')
        self.assertEqual(longestAlphabeticalString('abaflmnoa'), 'aflmno')
    def test_no_longest_substring(self):
        self.assertEqual(longestAlphabeticalString('zyma'), 'z')
    def test_empty_string(self):
        self.assertEqual(longestAlphabeticalString(''), '')

unittest.main(verbosity=2)
