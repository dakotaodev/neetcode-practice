class Node:

    def __init__(self, key:int, value:int):
        self.key, self.value=key, value
        self.prev, self.next=None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        # initialize ll pointers
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left        

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove from ll
            self.remove(self.cache[key])
            # add to ll
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #remove from ll
            self.remove(self.cache[key])
        # update cache
        self.cache[key]=Node(key,value)
        # add to ll
        self.insert(self.cache[key])
        # check for eviction
        if len(self.cache)>self.capacity:
            #remove from ll
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]                    

    def insert(self, node):
        # this will update what the right pointer references, as this is the MRU
        prev, nxt= self.right.prev, self.right
        prev.next, node.prev=node,prev
        node.next,nxt.prev=nxt,node
    
    def remove(self, node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev


