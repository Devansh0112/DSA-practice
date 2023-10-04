class MyHashMap:

    def __init__(self):
        self._keys = list()
        self._values = list()
        

    def put(self, key: int, value: int) -> None:
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def get(self, key: int) -> int:
        # print(key)
        # print(self._keys)
        # print(self._values)
        if key in self._keys:
            index = self._keys.index(key)
            return self._values[index]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self._keys:
            index = self._keys.index(key)
            self._keys.remove(key)
            self._values.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)