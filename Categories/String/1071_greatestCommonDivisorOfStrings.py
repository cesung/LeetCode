class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        size1, size2 = len(str1), len(str2)

        # make sure str1 >= str2
        if size1 < size2:
            self.gcdOfStrings(str2, str1)
        
        for length in range(size2, 0, -1):
            base = str2[:length]
            t1 = size1 // length
            t2 = size2 // length
            if (
                size1 % length == 0 and
                size2 % length == 0 and
                base * t1 == str1 and
                base * t2 == str2
            ):
                return base
        
        return ""
