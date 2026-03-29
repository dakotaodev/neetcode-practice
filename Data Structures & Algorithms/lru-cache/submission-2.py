class Node:
    def __init__(self, key: int, value:int):
        self.key,self.value=key,value
        self.prev,self.next=None,None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def insert(self,node:Node):
        prev,nxt=self.right.prev,self.right
        prev.next, node.prev=node,prev
        node.next,self.right.prev=self.right,node

    def remove(self,node: Node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev


