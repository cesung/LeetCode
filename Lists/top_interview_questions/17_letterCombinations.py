class Solution:

	from collections import defaultdict

    def __init__(self):
        self.num_to_digits = defaultdict(str, {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        })
        
    def dfs(self, pos, digits):    
        if pos == len(digits):
            return [""]
        
        ret = []
        for comb in self.dfs(pos + 1, digits):
            for ch in self.num_to_digits[digits[pos]]:
                ret.append(ch + comb)
                
        return ret
    
    # O(4^n * n) time | O(4^n * n) space
    def letterCombinations(self, digits):
        return list() if not digits else self.dfs(0, digits)
