class Solution:
    def is_palindrome(self, substring):
        size = len(substring)
        
        left, right = 0, size - 1
        while left <= right:
            if substring[left] != substring[right]:
                return False
            left += 1
            right -= 1
        
        return True

    def dfs(self, s, idx, substrings):
        if idx == self.size:
            self.ret.append(substrings[:])
            return
        
        for jdx in range(idx + 1, self.size + 1):
            if self.is_palindrome(s[idx:jdx]):
                self.dfs(s, jdx, substrings + [s[idx:jdx]])

    def partition(self, s: str) -> List[List[str]]:
        self.size = len(s)
        self.ret = []
        self.dfs(s, 0, [])

        return self.ret
