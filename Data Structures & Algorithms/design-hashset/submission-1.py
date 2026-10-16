class MyHashSet:

    def __init__(self):
        self.hashset = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        index = key %  10
        bucket = self.hashset[index]
        if key not in bucket:
            bucket.append(key)
        

    def remove(self, key: int) -> None:
        index = key %  10
        bucket = self.hashset[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = key %  10
        bucket = self.hashset[index]
        if key in bucket:
            return True
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)