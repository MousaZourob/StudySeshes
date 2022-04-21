class MyHashSet:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5
    
    def __init__(self):
        self.hash_set = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        hsh = self.eval_hash(key)
        
        if key not in self.hash_set[hsh]:
            self.hash_set[hsh].append(key)
            
    def remove(self, key: int) -> None:
        hsh = self.eval_hash(key)
        
        if key in self.hash_set[hsh]:
            self.hash_set[hsh].remove(key)

    def contains(self, key: int) -> bool:
        hsh = self.eval_hash(key)
        return key in self.hash_set[hsh]