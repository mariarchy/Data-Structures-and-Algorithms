# LEETCODE PROBLEM 727 - Remove Duplicates from a sorted array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# -----------------------------------------------------------------------------
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length. Do not allocate extra
# space for another array, you must do this by modifying the input array
# in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        start = 0
        while i < len(nums):
            if nums[start] < nums[i]:
                nums[start+1] = nums[i]
                start += 1
            i += 1


        return start + 1
