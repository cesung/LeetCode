class Solution:

    def __init__(self):
        self.haystack = ""
        self.needle = ""
        self.haystack_len = -1
        self.needle_len = -1

    def match(self, idx):
        for l in range(self.needle_len):
            if self.haystack[idx + l] != self.needle[l]:
                return False

        return True

    # O(n) time | O(1) space
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        self.haystack, self.needle = haystack, needle
        self.haystack_len, self.needle_len = len(haystack), len(needle)

        for idx in range(0, self.haystack_len - self.needle_len + 1):
            #print(idx)
            if self.match(idx):
                return idx

        return -1
