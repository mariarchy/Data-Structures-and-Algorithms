import unittest
from collections import defaultdict


def has_palindrome_permutation(the_string):
    # if all chars % 2 == 0 and 1 char % 2 == 1, then has_palindrome_permutation
    if len(the_string) < 2: return True

    c_counter = set()
    for c in the_string:
        if c in c_counter:
            c_counter.remove(c)
        else:
            c_counter.add(c)

    if not c_counter or len(c_counter) == 1: return True

    return False



# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
