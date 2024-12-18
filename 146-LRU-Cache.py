class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key 
        self.val = val
        self.prev = prev
        self.next = next
        
class LRUCache(object):

    def __init__(self, capacity):
        \\\
        :type capacity: int
        \\\
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def deleteNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def addNode(self, node):
        # Add node before tail (at end of actual list)
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        \\\
        :type key: int
        :rtype: int
        \\\
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.deleteNode(node)
        self.addNode(node)
        return node.val
        

    def put(self, key, value):
        \\\
        :type key: int
        :type value: int
        :rtype: None
        \\\
        if key in self.map:
            node = self.map[key]
            self.deleteNode(node)
            node.val = value
            self.addNode(node)
        else:
            if len(self.map) >= self.capacity:
                lru_node = self.head.next
                self.deleteNode(lru_node)
                del self.map[lru_node.key]
            
            new_node = Node(key, value)
            self.map[key] = new_node
            self.addNode(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)