class Solution:
    # O(1) time | O(1) space
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x or y:
            diff = x%2 != y%2
            cnt += 1 if diff else 0
            x >>= 1
            y >>= 1

        return cnt

class Solution2:
    # O(1) time | O(1) space
    def hammingDistance(self, x: int, y: int) -> int:

        # bin(), python build-in function
        return bin(x^y).count('1')
