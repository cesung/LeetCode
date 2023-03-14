class Solution:
    def is_overlap(self, interval1, interval2):
        return True if (
            interval2[0] <= interval1[0] <= interval2[1] or
            interval2[0] <= interval1[1] <= interval2[1] or
            interval1[0] <= interval2[0] and interval1[1] >= interval2[1]
        ) else False

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        size = len(intervals)
        
        ret = []
        for idx in range(size):
            if self.is_overlap(intervals[idx], new_interval):
                new_interval[0] = min(new_interval[0], intervals[idx][0])
                new_interval[1] = max(new_interval[1], intervals[idx][1])
            else:
                ret.append(intervals[idx])
        
        ret.append(new_interval)
        ret.sort()
        
        return ret
