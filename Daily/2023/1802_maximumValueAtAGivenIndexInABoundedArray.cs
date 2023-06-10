public class Solution {
    private long GetSum(long height, int n, int index) {
        long ttl = 0;
        if (height > index) {
            ttl += (height - index + height) * (index + 1) / 2;
        }
        else {
            ttl += index - height + 1;
            ttl += (1 + height) * height / 2;
        }

        if (height > n - index) {
            ttl += (height - (n - index) + 1 + height) * (n - index) / 2;
        }
        else {
            ttl += n - (index + height);
            ttl += (1 + height) * height / 2;
        }

        return ttl - height;
    }

    public int MaxValue(int n, int index, int maxSum) {
        int left = 1, right = maxSum;
        while (left < right) {
            int mid = right - (right - left) / 2;

            if (GetSum(mid, n, index) <= maxSum) {
                left = mid;
            }
            else {
                right = mid - 1;
            }
        }
        
        return left;
    }
}