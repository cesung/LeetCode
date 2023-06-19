public class Solution {
    public int FindMinDifference(IList<string> timePoints) {
        int n = timePoints.Count;

        HashSet<string> vis = new HashSet<string>();
        foreach (string timePoint in timePoints) {
            vis.Add(timePoint);
        }
        if (vis.Count != n) {
            return 0;
        }

        List<int> times = new List<int>();
        foreach (string timePoint in timePoints) {
            string[] segs = timePoint.Split(':');
            times.Add( Convert.ToInt32(segs[0]) * 60 + Convert.ToInt32(segs[1]) );
        }
        times.Sort();
        
        int min_diff = Int32.MaxValue;
        for (int idx = 1; idx < n; idx++) {
            min_diff = Math.Min(
                min_diff,
                times[idx] - times[idx - 1]
            );
        }

        int max_time = 24 * 60;
        min_diff = Math.Min(
            min_diff,
            (max_time - times[n - 1]) + times[0]
        );

        return min_diff;
    }
}