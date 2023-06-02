public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var vis = new HashSet<int>();
        var rcd  = new Dictionary<int, int>();

        foreach (var (num, idx) in nums.Select((num, idx) => (num, idx))) {
            if (vis.Contains(target - num)) {
                return new int[] {idx, rcd[target - num]};
            }
            vis.Add(num);
            if (!rcd.ContainsKey(num)) rcd.Add(num, idx);
        }

        return new int[] {-1, -1};
    }
}
