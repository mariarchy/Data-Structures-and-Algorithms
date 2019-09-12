import unittest
# [1,3,5]
# [2,4]
# [1,2,3,4,5,6]
# ord1 entirely < ord2
# ord2 entirely < ord1
# some in ord1 are < ord2
# empty cases: both empty, one empty
#

# while ptr < length:
#       while val @ ptr1 <= val @ ptr2: append val @ ptr1 to res & ptr1++
#       while val @ ptr2 <= val @ ptr1: append val @ ptr2 to res & ptr2++
# append
def merge_lists(ord1, ord2):
    if not ord1: return ord2
    if not ord2: return ord1
    if ord1[len(ord1)-1] < ord2[0]: return ord1 + ord2
    if ord2[len(ord2)-1] < ord1[0]: return ord2 + ord1

    ptr1 = ptr2 = 0
    res = []
    while ptr1 < len(ord1) and ptr2 < len(ord2):
        if ord1[ptr1] <= ord2[ptr2]:
            res.append(ord1[ptr1])
            ptr1 += 1
        else:
            res.append(ord2[ptr2])
            ptr2 += 1

    while ptr1 < len(ord1):
        res.append(ord1[ptr1])
        ptr1 += 1

    while ptr2 < len(ord2):
        res.append(ord2[ptr2])
        ptr2 += 1

    return res

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
