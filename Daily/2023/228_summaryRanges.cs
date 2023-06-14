public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        int n = nums.Length;
        if (n == 0) {
            return new List<string>();
        }

        int prev = nums[0];

        List<string> ret = new List<string>();
        for (int idx = 1; idx < n + 1; idx++) {
            if (idx == n) {
                ret.Add(
                    prev == nums[idx - 1] ?
                    $"{prev}" :
                    $"{prev}->{nums[idx - 1]}"
                );
                break;
            }
            if (nums[idx] != nums[idx - 1] + 1) {
                ret.Add(
                    prev == nums[idx - 1] ?
                    $"{prev}" :
                    $"{prev}->{nums[idx - 1]}"
                );
                prev = nums[idx];
            }
        }

        return ret;
    }
}