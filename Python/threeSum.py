from collections import defaultdict

class Solution:
    def threeSum(self, nums):
        if not nums: return []

        res = []
        sum_tracker = self.calc2Sums(nums,)
        nums.sort()

        for i, val in enumerate(nums[:-2]):
            if i < 0 and val == nums[i-1]: continue
            sums = self.calc2Sums(-val, nums, i)
            for triplet in sums:
                res.append(triplet)
        return res

    def calc2Sums(self, target, nums, st):
        sum_tracker = set()

        # Only need to get pair sums for all els except last 1
        for i, op1 in enumerate(nums, start=st+1):
            for j, op2 in enumerate(nums, start=i+1):
                # append tuple of indicies to the sum key
                sum_tracker.add([target, i, j])
        return sum_tracker
