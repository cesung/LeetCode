from typing import *


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.length = length
        self.rcd = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        if (
            self.rcd[index] and
            self.rcd[index][-1][0] == self.snap_id
        ):
            self.rcd[index][-1][1] = val
        else:
            self.rcd[index].append( [self.snap_id, val] )

    def snap(self) -> int:
        ret = self.snap_id
        self.snap_id += 1

        return ret

    def get(self, index: int, snap_id: int) -> int:
        # error handling
        if index >= self.length:
            return -1

        if index not in self.rcd:
            return 0

        left, right = 0, len(self.rcd[index]) - 1

        while left < right:
            mid = left + (right - left) // 2 + 1
            if self.rcd[index][mid][0] > snap_id:
                right = mid - 1
            else:
                left = mid

        return self.rcd[index][left][1] if self.rcd[index][left][0] <= snap_id else 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)