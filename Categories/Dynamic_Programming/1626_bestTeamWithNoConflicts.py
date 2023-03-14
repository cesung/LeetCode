class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        size = len(scores)

        lst = [ (age, score) for age, score in zip(ages, scores)]
        # sort by age, break tie via score
        lst.sort(key = lambda x : (x[0], x[1]))

        dp = [lst[idx][1] for idx in range(size)]
        ret = dp[0]
        for idx in range(1, size):
            for jdx in range(idx):
                if lst[idx][1] >= lst[jdx][1]:
                    dp[idx] = max(
                        dp[idx],
                        dp[jdx] + lst[idx][1]
                    )
                
            ret = max(
                ret,
                dp[idx],
            )

        return ret
