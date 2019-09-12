import unittest

#   [Meeting(0, 1), Meeting(3, 5), Meeting(4, 8), Meeting(10, 12), Meeting(9, 10)]
# Return   [Meeting(0, 1), Meeting(3, 8), Meeting(9, 12)]

#   [Meeting(9, 10), Meeting(4, 8), Meeting(0, 1), Meeting(3, 5), Meeting(10, 12)]
# Return   [Meeting(0, 1), Meeting(3, 8), Meeting(9, 12)]

# tracker
#
# for start and end: if start and end are marked break
#                    if start is marked (but end not marked), mark index start -> end - 1
#                    if end is marked (but start not marked), mark index start -> end - 1
#                    if start and end not marked, mark index start -> end - 1
# iterate through array and if index is marked, loop until not marked and append to final list
# optimization: mark only if unmarked, redundant to mark indices more than once

# tests
# empty list, meetings that don't overlap, meetings w/ some overlap, meetings that all overlap

def merge_ranges(meetings):
    #   [Meeting(9, 10), Meeting(4, 8), Meeting(0, 1), Meeting(3, 5), Meeting(10, 12)]
    # Return   [Meeting(0, 1), Meeting(3, 8), Meeting(9, 12)]
    # [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
    if not meetings: return []

    res = []
    max = find_max(meetings)

    tracker = [0] * (max + 1)
    # Merge meeting ranges
    for meeting in meetings:
        start = meeting[0]
        end = meeting[1]

        for i in range(start, end):
            tracker[i] = 1

    in_meeting = False
    start = 0
    for i in range(len(tracker)):
        if tracker[i] and not in_meeting:
            in_meeting = True
            start = i
        if (not tracker[i] or i == len(res) - 1) and in_meeting:
            in_meeting = False
            res.append((start, i))

    return res

def find_max(meetings):
    max = meetings[0][1]

    # Find the size of the array
    for meeting in meetings:
        if meeting[1] > max: max = meeting[1]

    return max












# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
