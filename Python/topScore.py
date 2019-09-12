import unittest

# unsorted_scores = [2, 1, 3]
# H = 4
# sorted = [0, 1, 1, 1, 0]
# [3,2,1]
# highest score
def sort_scores(unsorted_scores, highest_possible_score):
    if not unsorted_scores: return []

    score_chart = [0] * (highest_possible_score + 1)
    for score in unsorted_scores:
        score_chart[score] += 1

    res = []
    for i in range(highest_possible_score, -1, -1):
        for j in range(score_chart[i]):
            res.append(i)

    return res



# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
