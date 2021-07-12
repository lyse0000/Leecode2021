Trie = lambda: collections.defaultdict(Trie)
class FileSystem:

    def __init__(self):
        self.fs = Trie()
        self.info = collections.defaultdict(str)
        
    def ls(self, path: str) -> List[str]:
        if path in self.info:
            return path.split('/')[-1:]
        node = self.fs
        for p in path.split('/'):
            if p in node:
                node = node[p]
            elif p:
                return []
        return sorted(node.keys())
                
    def mkdir(self, path: str) -> None:
        node = self.fs
        for p in path.split('/'):
            if p: node = node[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.info[filePath] += content
        

    def readContentFromFile(self, filePath: str) -> str:
        return self.info[filePath]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
