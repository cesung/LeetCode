public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        int n = nums.Length;
        // left : swap destination
        // right: current pointer
        int left = 0, right = 0, prev = -101;
        while (right < n)
        {
            if (nums[right] != prev)
            {
                nums[left] = nums[right];
                left++;
            }

            prev = nums[right];
            right++;
        }

        return left;
    }
}