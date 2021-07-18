class TrieNode():
    def __init__(self):
        self.next = {}
        self.word = None
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, w):
        node = self.root
        for c in w:
            if c not in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
        node.word = w

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        tree = Trie()
        for w in words:
            tree.insert(w)
        nodes = []
        boolean = [False]*len(s)
        
        for i in range(len(s)):
            temp = []
            nodes.append(tree.root)
            for node in nodes:
                if s[i] in node.next:
                    node = node.next[s[i]]
                    temp.append(node)
                    if node.word:
                        boolean[i+1-len(node.word):i+1] = [True]*len(node.word)
            nodes = temp
            
        ret, i = "", 0
        while i < len(s):
            if boolean[i]:
                ret+="<b>"
                while(i < len(s) and boolean[i]):
                    ret+=s[i]
                    i+=1
                ret+="</b>"
            if i<len(s): ret+=s[i]
            i+=1
                
        return ret
        
