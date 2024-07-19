class Empty(Exception):
    pass


class PriorityQueueBase:
    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def __repr__(self):
            return "({0},{1})".format(self._key, self._value)

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        raise NotImplementedError("must be implemented by subclass")

    def add(self, key, value):
        raise NotImplementedError("must be implemented by subclass")

    def min(self):
        raise NotImplementedError("must be implemented by subclass")

    def remove_min(self):
        raise NotImplementedError("must be implemented by subclass")


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        # Insert in sorted order
        for i in range(len(self._data)):
            if newest < self._data[i]:
                self._data.insert(i, newest)
                break
        else:
            self._data.append(newest)

    def min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data.pop(0)
        return (item._key, item._value)


# Example usage
if __name__ == "__main__":
    pq = SortedPriorityQueue()
    pq.add(5, "A")
    pq.add(9, "C")
    pq.add(3, "B")
    pq.add(7, "D")

    print("Min:", pq.min())  # Should print (3, 'B')
    print("Remove Min:", pq.remove_min())  # Should remove and print (3, 'B')
    print("Min:", pq.min())  # Should print (5, 'A')
