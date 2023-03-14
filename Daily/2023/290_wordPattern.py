from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ptn_size = len(pattern)
        words = s.split()
        words_size = len(words)

        if ptn_size != words_size:
            return False

        ptn_to_word = defaultdict(str)
        word_to_ptn = defaultdict(str)

        for ptn, word in zip(pattern, s.split()):
            if (
                (word in word_to_ptn and word_to_ptn[word] != ptn) or
                (ptn in ptn_to_word and ptn_to_word[ptn] != word)
            ):
                return False
            
            ptn_to_word[ptn], word_to_ptn[word] = word, ptn
        
        return True
