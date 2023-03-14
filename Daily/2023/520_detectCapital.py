class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        is_all_cap, is_all_non_cap, is_first_cap = True, True, True
        for idx, ch in enumerate(word):
            if idx == 0 and ord('a') <= ord(ch) <= ord('z'):
                is_first_cap = False
            
            if ord('a') <= ord(ch) <= ord('z'):
                is_all_cap = False
            
            if ord('A') <= ord(ch) <= ord('Z'):
                is_all_non_cap = False
                if idx > 0:
                    is_first_cap = False
        
        return True if (
            is_all_cap or
            is_all_non_cap or
            is_first_cap
        ) else False
