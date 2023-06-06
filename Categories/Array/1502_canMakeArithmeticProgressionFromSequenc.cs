public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        int n = arr.Length
        Array.Sort(arr)

        int diff = arr[1] - arr[0]

        for (int idx=2
             idx < n
             idx++) {
            if (arr[idx] - arr[idx - 1] != diff) {
                return false
            }
        }

        return true
    }
}
