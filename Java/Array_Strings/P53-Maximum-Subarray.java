// LEETCODE PROBLEM 53 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/
// -----------------------------------------------------------------------------
// Given an integer array nums, find the contiguous subarray (containing at least
// one number) which has the largest sum and return its sum.

class Solution {
  public int maxSubArray(int[] nums) {
    if (nums.length == 0) return 0;
    int max_sum, curr_sum;
    max_sum = curr_sum = nums[0];
    for (int i = 0; i < nums.length - 1; i++) {
      curr_sum = (nums[i+1] > curr_sum + nums[i+1]) ? nums[i+1] : curr_sum + nums[i+1];
      max_sum = (max_sum > curr_sum) ? max_sum : curr_sum;
    }
    return max_sum;
  }
}

// Using Math.max and condensing initialization
class Solution2 {
  public int maxSubArray2(int[] nums) {
    if (nums.length == 0) return 0;
    int max_sum = nums[0], curr_sum = nums[0];
    for (int i = 0; i < nums.length - 1; i++) {
      curr_sum = Math.max(nums[i+1], curr_sum + nums[i+1]);
      max_sum = Math.max(max_sum, curr_sum);
    }
    return max_sum;
  }
}
