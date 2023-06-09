public class Solution {
    public int SearchInsert(int[] nums, int target) {
        int n = nums.Length;
        int left = 0, right = n - 1;

        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }

        return nums[left] < target ? left + 1: left;
    }
}