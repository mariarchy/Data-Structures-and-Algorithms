// LEETCODE PROBLEM 26 - Remove Duplicates from a sorted array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
// -----------------------------------------------------------------------------
// Given a sorted array nums, remove the duplicates in-place such that each
// element appear only once and return the new length. Do not allocate extra
// space for another array, you must do this by modifying the input array
// in-place with O(1) extra memory.

class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int ptr1 = 0;
        int ptr2 = 1;
        boolean dupe = false;
        while (ptr2 < nums.length) {
            if (nums[ptr1] == nums[ptr2]) {
                dupe = true;
            } else {
                ptr1++;
                if (dupe) {
                    nums[ptr1] = nums[ptr2];
                }
            }
            ptr2++;
        }

        return ptr1 + 1;
    }

    // Improved Solution
    public int removeDuplicates2(int[] nums) {
        if (nums.length == 0) return 0;

        int ptr1 = 0;
        int ptr2 = 1;
        while (ptr2 < nums.length) {
            // A boolean check to see if the previous pair was a duplicate is
            // unneeded because regardless, the result of line 41 and 42 should
            // be the same.
            if (nums[ptr1] != nums[ptr2]) {
                ptr1++;
                nums[ptr1] = nums[ptr2];
            }
            ptr2++;
        }

        return ptr1 + 1;
    }
}
