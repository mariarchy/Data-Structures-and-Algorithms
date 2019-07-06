class Solution {
    public int firstUniqChar(String s) {
      int[] chars = new int[26];
      for (int i = 0; i < s.length(); i++) {
        chars[s.charAt(i) - 'a']++;
      }
      for (int i = 0; i < s.length(); i++) {
        if (chars[s.charAt(i) - 'a'] == 1) return i;
      }
      return -1;
    }
  }


// Improvement
// It seems as though there is a better runtime when converting the string to
// an array and avoiding Java's charAt method.
class Solution {
    public int firstUniqChar(String s) {
      int[] chars = new int[26];
      char[] arr = s.toCharArray();
      for (char c : arr) {
        chars[c - 'a']++;
      }
      for (int i = 0; i < arr.length; i++) {
        if (chars[arr[i] - 'a'] == 1) return i;
      }
      return -1;
    }
  }
