class Solution {
public:
    // O(n) time | O(1) space
    // Buttom-up DP, rolling memory
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        int* rcd = new int[2];  // O(1) memory usage
        rcd[0] = nums[0];
        rcd[1] = max(rcd[0], nums[1]);

        for (int i = 2; i < nums.size(); i++) {
            int maxv = max(rcd[0] + nums[i], rcd[1]);
            rcd[0] = rcd[1];
            rcd[1] = maxv;
        }

        return rcd[1];
    }
};
