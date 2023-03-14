class Solution:
    # O(log(n)) time | O(1) space
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            if n%3:
                return False
            n //= 3
            
        return True
