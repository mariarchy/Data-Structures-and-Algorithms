# LEETCODE PROBLEM 53 - Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# -----------------------------------------------------------------------------
# Given an integer array nums, find the contiguous subarray (containing at least
# one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        max_sum = curr_sum = nums[0]
        for i in range(len(nums)-1):
            curr_sum = max(curr_sum + nums[i+1], nums[i+1])
            max_sum = max(max_sum, curr_sum)
        return max_sum
