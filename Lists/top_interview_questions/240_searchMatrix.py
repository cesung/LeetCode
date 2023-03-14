class Solution:
    def search(self, matrix, target, row, col, M, N):
        # boundary check
        if row == M or col < 0:
            return False

        if matrix[row][col] == target:
            return True

        # move left
        elif matrix[row][col] > target:
            return self.search(matrix, target, row, col - 1, M, N)

        # move bot
        elif matrix[row][col] < target:
            return self.search(matrix, target, row + 1, col, M, N)

    # O(n + m) time | O(1) space
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        return self.search(matrix, target, 0, N - 1, M, N)
