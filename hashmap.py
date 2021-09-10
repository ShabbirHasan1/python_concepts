class HashTable(object):
    def __init__(self):
        self._size = 10
        self.hashmap = [[] for _ in range(0, self._size)]

    def _hash(self,key):
        return hash(key) % self._size

    def set(self, key, value):
        i_list = self.hashmap[self._hash(key)]
        for i, ituple in enumerate(i_list):
            ikey, ivalue = ituple
            if key == ikey:
                i_list[i] = (key, value)
                return
        i_list.append((key, value))
        return

    def get(self, key):
        i_list = self.hashmap[self._hash(key)]
        for ituple in i_list:
            ikey, ivalue = ituple
            if key == ikey:
                return ivalue
            else:
                raise KeyError('Key does not exist.')

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


if __name__ == "__main__":
    mymap = HashTable()
    mymap.set('a',1)
    mymap.set('b', 2)

    print(mymap['a'])
    print(mymap['b'])
    print(mymap.hashmap)