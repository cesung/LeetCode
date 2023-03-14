from sortedcontainers import SortedDict

class SummaryRanges1:

    def __init__(self):
        self.sorted_dict = SortedDict()
        

    def addNum(self, value: int) -> None:
        self.sorted_dict[value] = True
        

    def getIntervals(self) -> List[List[int]]:
        ret = []
        for n in self.sorted_dict:
            if ret and ret[-1][1] == n - 1:
                ret[-1][1] = n
            else:
                ret.append([n, n])
        
        return ret
        

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()


class SummaryRanges2:

    def __init__(self):
        self.vis = set()
        self.arr = []
        
    def addNum(self, value: int) -> None:
        if value in self.vis:
            return
        
        self.vis.add(value)
        if not self.arr:
            self.arr.append(value)
            return
        
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] < value:
                left = mid + 1
            else:
                right = mid
        
        if self.arr[left] < value:
            self.arr.insert(len(self.arr), value)
        else:
            self.arr.insert(left, value)
        
    def getIntervals(self) -> List[List[int]]:
        ret = []
        for n in self.arr:
            if ret and ret[-1][1] == n - 1:
                ret[-1][1] = n
            else:
                ret.append([n, n])
        
        return ret
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
