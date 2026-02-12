class Dictionary:

    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def _get_index(self, key: int) -> int:
        return hash(key) % self.capacity

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            if node is not None:
                self[node[0]] = node[2]

    def __setitem__(self, key: int, value: int) -> None:

        if self.size / self.capacity >= 2 / 3:
            self._resize()

        index = self._get_index(key)
        node = self.table[index]

        if node is None:
            self.table[index] = [key, hash(key), value]
            self.size += 1
            return
        elif node[0] == key:
            self.table[index][2] = value
            return

        i = (index + 1) % self.capacity
        while self.table[i] is not None:
            if self.table[i][0] == key:
                self.table[i][2] = value
                return
            i = (i + 1) % self.capacity

        self.table[i] = [key, hash(key), value]
        self.size += 1

    def __getitem__(self, key: int) -> int:
        index = self._get_index(key)
        node = self.table[index]

        if node is None:
            raise KeyError(key)

        if node[0] == key:
            return node[2]

        i = (index + 1) % self.capacity
        while self.table[i] is not None:
            if self.table[i][0] == key:
                return self.table[i][2]
            i = (i + 1) % self.capacity

        raise KeyError(key)

    def __len__(self) -> int:
        return self.size
