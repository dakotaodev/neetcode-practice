class Node:

    def __init__(self, key, val):
        self.val=val
        self.key=key
        self.next,self.prev=None,None

class LRUCache:

    def __init__(self, capacity: int):
       self.cache: dict[int,Node]={}
       self.capacity=capacity
       self.left,self.right=Node(0,0),Node(0,0)
       self.left.next,self.right.prev=self.right,self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove Node
            self.remove(self.cache[key])
            # add node
            self.add(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key,value)
        self.cache[key]=node
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def add(self, node: Node):
        prev,next=self.right.prev, self.right
        prev.next,node.prev=node, prev
        node.next,self.right.prev=self.right, node

    def remove(self, node: Node):
        prev,next=node.prev, node.next
        prev.next,next.prev=next,prev



