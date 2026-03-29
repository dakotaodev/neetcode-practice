
class Node:

    def __init__(self,key,val):
        self.val=val
        self.key=key
        self.prev,self.next=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={} 
        self.right,self.left=Node(0,0),Node(0,0)
        self.right.prev,self.left.next=self.left,self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node:Node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev

    def insert(self, node:Node):
        prev,nxt=self.right.prev,self.right
        prev.next,node.prev=node,prev
        node.next,nxt.prev=nxt,node  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]





