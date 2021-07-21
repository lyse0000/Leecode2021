class Trie():
    def __init__(self):
        self.next = {}
        self.data = set()
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.cache = ""
        self.root = Trie()
        self.rank = {}
        for s, t in zip(sentences, times):
            self.addSentence(s, t)
        
    def addSentence(self, s, t):
        node = self.root
        node.data.add(s)
        for c in s:
            if c not in node.next:
                node.next[c] = Trie()
            node = node.next[c]
            node.data.add(s)
        self.rank[s] = self.rank.get(s, 0) - t
    
    def search(self, word):
        node = self.root
        ret = []
        for c in word:
            if c not in node.next:
                return []
            node = node.next[c]
        for s in node.data:
            ret.append([self.rank[s], s])
        ret = sorted(ret, key = lambda x: (x[0],x[1]))[:3]
        return [r[1] for r in ret] 
    
    def input(self, c: str) -> List[str]:
        ret = []
        if c == "#":
            self.addSentence(self.cache, 1)
            self.cache = ""
            
        else:
            self.cache += c
            ret = self.search(self.cache)
            return ret
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
