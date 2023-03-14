from collections import defaultdict

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        size = len(words)
        word_order = defaultdict(int, {
            " " : -1
        })

        for idx, ch in enumerate(order):
            word_order[ch] = idx
        
        for idx in range(1, size):
            prev_word_length = len(words[idx - 1])
            post_word_length = len(words[idx])

            for jdx in range(max(prev_word_length, post_word_length)):
                prev_word = words[idx - 1][jdx] if jdx < prev_word_length else " "
                post_word = words[idx][jdx] if jdx < post_word_length else " "
                if word_order[prev_word] < word_order[post_word]:
                    break
                elif word_order[prev_word] > word_order[post_word]:
                    return False

        return True
