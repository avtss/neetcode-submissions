class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if key in self.arr:
            return
        else:
            self.arr.append(key)
            return

    def remove(self, key: int) -> None:
        if key in self.arr:
            self.arr.remove(key)
            return
        else:
            return

    def contains(self, key: int) -> bool:
        if key in self.arr:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)