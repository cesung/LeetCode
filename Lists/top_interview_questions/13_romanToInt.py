class Solution:
    # O(n) time | O(1) space
    def romanToInt(self, s):
        roman_to_int = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        ret = roman_to_int[ s[0] ]
        for idx in range(1, len(s)):
            ret += roman_to_int[ s[idx] ]
            if roman_to_int[ s[idx] ] > roman_to_int[ s[idx - 1] ]:
                ret -= 2*roman_to_int[ s[idx - 1] ]

        return ret
