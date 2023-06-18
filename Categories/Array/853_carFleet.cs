public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        int n = position.Length;
        List<Tuple<int,int>> pairs = new List<Tuple<int, int>>();

        for (int idx = 0; idx < n; idx++) {
            pairs.Add(new Tuple<int,int>(position[idx], speed[idx]));
        }

        pairs = pairs.OrderBy(p => p.Item1).ToList();

        int prev = n - 1;
        int ret = 1;
        for (int idx = n - 2; idx >= 0; idx--) {
            double t_prev = (double)(target - pairs[prev].Item1) / pairs[prev].Item2;
            double t_cur = (double)(target - pairs[idx].Item1) / pairs[idx].Item2;
            if (t_cur > t_prev) {
                ret += 1;
                prev = idx;
            }
        }

        return ret;
    }
}