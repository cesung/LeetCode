from typing import *

class Solution:
    def dfs(self, limit, idx):
        if idx == self.n:
            return True
        
        # Distribue idx'th cookie to someone who have not received any cookie
        flag = False
        for jdx in range(self.k):
            
            if self.rcd[jdx] + self.cookies[idx] > limit:
                continue

            # if the jdx'th person have not received any cookie
            if self.rcd[jdx] == 0:
                # idx'th cookie already distribute to someone like jdx (who have not received any cookie), skip this kind of distribution
                if flag == True:
                    continue
                # if not, mark it as True to prevent same distribution next time
                flag = True

            self.rcd[jdx] += self.cookies[idx]

            # early stop
            if self.dfs(limit, idx + 1):
                return True

            # backtracking
            self.rcd[jdx] -= self.cookies[idx]
        
        return False

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        INF = 2147483647

        self.rcd = [0 for _ in range(k)]

        # sort the cookies reversely to hit the limit faster
        cookies.sort(reverse=True)
        self.cookies = cookies

        self.n = len(cookies)
        self.k = k

        left, right = 1, INF
        while left < right:
            mid = left + (right - left) // 2

            for idx in range(k):
                self.rcd[idx] = 0

            if not self.dfs(mid, 0):
                left = mid + 1
            else:
                right = mid
        
        return left