class Node:
    def __init__(self, key:int, val:int):
        self.key=key
        self.val=val
        self.next:Node=None
        self.prev:Node=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache:dict[int,Node]={}        
        self.capacity=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next,self.right.prev=self.right,self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        node=Node(key,value)
        self.cache[key]=node
        self.add(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node: Node) -> None:
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev

    def add(self, node: Node) -> None:
        prev,next=self.right.prev, self.right
        prev.next, next.prev=node,node
        node.prev,node.next=prev,next
        
