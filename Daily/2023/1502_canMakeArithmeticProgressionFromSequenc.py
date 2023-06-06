class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        diff = arr[1] - arr[0]
        for idx in range(2, n):
            if arr[idx] - arr[idx - 1] != diff:
                return False

        return True
