class Node:
    def __init__(self, key, value):
        self.freq = 1
        self.value = value
        self.key = key
        self.prev = None
        self.nexr = None
            
class LFUCache:
    

    def __init__(self, capacity: int):
        self.freqDict = {}
        #self.frequencies = [] # use to pop the least fre
        self.data = {}
        self.capacity = capacity
        self.count = 0

    def removeNodeFromFrq(self, node, f):
        self.data.pop(node.key)
        self.count -= 1
        
        _prev = node.prev
        _next = node.next
        if _prev == _next: # the last or only element in freqlist
            self.freqDict.pop(f)
            return
        node.prev.next = _next
        node.next.prev = _prev
    
    def addNodeToFrq(self, node, f):
        self.data[node.key] = node
        self.count += 1
        
        if f in self.freqDict:
            head = self.freqDict[f]
            headnext = head.next
            head.next = node
            node.next = headnext
            node.prev = head
            headnext.prev = node
        else:
            head = Node(-1, -1)
            head.prev = node
            head.next = node
            node.prev = head
            node.next = head
            self.freqDict[f] = head
            
    def updatedata(self, key):
        node = self.data[key]
        self.removeNodeFromFrq(node, node.freq)
        
        node.freq += 1
        self.addNodeToFrq(node, node.freq)
    
    def get(self, key: int) -> int:
        if key not in self.data:
            #print(self.data)
            return -1
        self.updatedata(key)
        return self.data[key].value
    
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key].value = value
            self.updatedata(key)
        else:
            node = Node(key, value)
            if self.count >= self.capacity and self.count>0:
                minFreq = min(self.freqDict.keys())
                lastNode = self.freqDict[minFreq].prev
                self.removeNodeFromFrq(lastNode, minFreq)
            if self.count+1<=self.capacity:
                self.addNodeToFrq(node, 1)
            
        
"""
["LFUCache","put","put","get","put","get","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]


["LFUCache","put","put","get","get"]
[[0],[0,0],[0,0],[0],[0]]
"""

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
