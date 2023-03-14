from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        size = len(fruits)

        cntr = defaultdict(int)
        vis = set()

        idx = 0
        while idx < size:
            if fruits[idx] not in vis and len(vis) == 2:
                break
            cntr[fruits[idx]] += 1
            vis.add(fruits[idx])
            idx += 1
        
        max_num_fruits = idx

        left = 0
        for right in range(idx, size):
            if fruits[right] not in vis:
                while len(vis) == 2:
                    cntr[fruits[left]] -= 1
                    if cntr[fruits[left]] == 0:
                        vis.remove(fruits[left])
                    left += 1
                vis.add(fruits[right])
            cntr[fruits[right]] += 1
            
            max_num_fruits = max(
                max_num_fruits,
                right - left + 1,
            )
            
        return max_num_fruits
