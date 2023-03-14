class Solution {
public:

    // O(NM) time -> TLE
    // Top-down DP
    bool dp(int cur_idx,
            vector<int> &nums,
            vector<bool> &vis,
            vector<bool> &can_jump,
            int N) {

        if (vis[cur_idx] == true) {
            return can_jump[cur_idx];
        }

        vis[cur_idx] = true;

        if (cur_idx + nums[cur_idx] >= N - 1) {
            can_jump[cur_idx] = true;
        } else {
            bool suc = false;
            for (int step = 1; step <= nums[cur_idx]; step++) {
                suc |= dp(cur_idx + step, nums, vis, can_jump, N);
            }
            can_jump[cur_idx] = suc;
        }

        return can_jump[cur_idx];
    }

    bool canJump(vector<int>& nums) {
        int N = nums.size();
        vector<bool> vis(N, false);
        vector<bool> can_jump(N, false);
        return dp(0, nums, vis, can_jump, N);
    }
};


class Solution2 {
public:
    // O(NM) time -> AC
    // Buttom-up DP
    bool canJump(vector<int>& nums) {
        int N = nums.size();
        vector<bool> dp(N, false);
        dp[N-1] = true;
        for (int i = N - 1; i >= 0; i--) {
            if (i + nums[i] >= N - 1) {
                dp[i] = true;
            } else {
                bool suc = false;
                for (int step = 1; step <= nums[i]; step++) {
                    suc |= dp[i + step];
                }
                dp[i] = suc;
            }
        }
        return dp[0];
    }
};
