class Solution:
    # Greedy
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for cur_idx, num in enumerate(nums):
            if cur_idx > max_idx:
                return False
            max_idx = max(max_idx, cur_idx + nums[cur_idx])
        return True

class Solution2:
    # O(NM) time -> TLE
    # Buttom-up DP
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False for _ in range(N)]
        dp[N - 1] = True
        for i in reversed(range(N - 1)):
            if i + nums[i] >= N - 1:
                dp[i] = True
            else:
                suc = False
                for step in range(1, nums[i] + 1):
                    suc |= dp[i + step]
                dp[i] = suc

        return dp[0]

class Solution3:

    def __init__(self):
        self.vis = None

    def dp(self, idx, nums, N):

        if self.vis[idx] is not None:
            return self.vis[idx]

        if idx + nums[idx] >= N-1:
            self.vis[idx] = True

        else:
            suc = False
            for step in range(1, nums[idx] + 1):
                suc |= self.dp(idx + step, nums, N)

            self.vis[idx] = suc

        return self.vis[idx]

    # O(NM) time -> TLE
    # Top-down DP
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        self.vis = [None for _ in range(N) ]
        return = self.dp(0, nums, N)

