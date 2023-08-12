from typing import *
import sys

class Solution:
    def makeArraySortedByRemoving(self, num_removal):
        # removal boundary
        left, right = 0, num_removal - 1
        while right < self.n:
            left_suc = self.is_nondecreasing_from_left[left - 1] if left != 0 else True
            right_suc = self.is_nondecreasing_to_right[right + 1] if right != self.n - 1 else True
            left_bound = self.arr[left - 1] if left != 0 else -self.INF
            right_bound = self.arr[right + 1] if right != self.n - 1 else self.INF

            if (
                left_suc and
                right_suc and
                left_bound <= right_bound
            ):
                return True

            left += 1
            right += 1
        
        return False

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        self.INF = sys.maxsize
        self.n = len(arr)
        self.arr = arr
        
        # O(n)
        self.is_nondecreasing_from_left = [True for _ in range(self.n)]
        for idx in range(1, self.n):
            self.is_nondecreasing_from_left[idx] = (
                self.is_nondecreasing_from_left[idx - 1] & 
                (arr[idx] >= arr[idx - 1])
            )
            
        # O(n)
        self.is_nondecreasing_to_right = [True for _ in range(self.n)]
        for idx in range(self.n - 2, -1, -1):
            self.is_nondecreasing_to_right[idx] = (
                self.is_nondecreasing_to_right[idx + 1] &
                (arr[idx] <= arr[idx + 1])
            )
        
        left, right = 0, self.n
        while left < right:
            mid = left + (right - left) // 2
            if self.makeArraySortedByRemoving(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
S = Solution()
print(S.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]), 3)
print(S.findLengthOfShortestSubarray([5,4,3,2,1]), 4)
print(S.findLengthOfShortestSubarray([1,2,3]), 0)