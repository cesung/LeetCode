public class Solution {
    public int LargestAltitude(int[] gain) {
        int n = gain.Length;
        int max_alt = 0, cur_alt = 0;

        for (int idx = 0; idx < n; idx++) {
            cur_alt += gain[idx];
            max_alt = Math.Max(
                max_alt,
                cur_alt
            );
        }
    
        return max_alt;
    }
}