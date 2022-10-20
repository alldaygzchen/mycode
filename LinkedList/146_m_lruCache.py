class Node:

    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev = self.next = None



class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {} #key=>node
        self.cap =capacity

        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev,nxt = node.prev,node.next # why use double linked list
        prev.next,nxt.prev = nxt,prev

    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        nxt.prev =node
        prev.next = node
        node.prev =prev
        node.next = nxt
        

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] #why save key in node