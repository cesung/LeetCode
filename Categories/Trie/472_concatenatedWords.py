from collections import defaultdict

class Trie:
    def __init__(self):
        self.neighbors = defaultdict(Trie)
        self.is_end = False
    
    def insert(self, word):
        node = self
        for ch in word:
            node = node.neighbors[ch]
        node.is_end = True

class Solution:

    def dfs(self, word, word_size, cur, vis):
        if cur == word_size:
            return True

        if cur in vis:
            return vis[cur]

        node = self.trie

        for idx in range(cur, word_size):
            if word[idx] in node.neighbors:
                node = node.neighbors[word[idx]]
                if node.is_end and self.dfs(word, word_size, idx + 1, vis):
                    vis[cur] = True
                    return True
            else:
                break

        vis[cur] = False
        return vis[cur]
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x : len(x))
        self.trie = Trie()

        ret = []
        for word in words:
            vis = defaultdict(bool)
            if self.dfs(word, len(word), 0, vis):
                ret.append(word)
            self.trie.insert(word)

        return ret
