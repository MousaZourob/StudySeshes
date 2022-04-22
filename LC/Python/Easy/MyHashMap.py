class ListNode:
    def __init__(self, key, val, nxt):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:
    def eval_hash(self, key):
        return key * self.mult % self.size
    
    def __init__(self):
        self.size = 19997
        self.mult = 1031237
        self.hash_map = [None] * 19997

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        hsh = self.eval_hash(key)
        self.hash_map[hsh] = ListNode(key, value, self.hash_map[hsh])

    def get(self, key: int) -> int:
        hsh = self.eval_hash(key)
        curr = self.hash_map[hsh]
        while curr:
            if curr.key == key: return curr.val
            curr = curr.next
            
        return -1

    def remove(self, key: int) -> None:
        hsh = self.eval_hash(key)
        curr = self.hash_map[hsh]
        
        if not curr: return
        
        if curr.key == key:
            self.hash_map[hsh] = curr.next
            return
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)