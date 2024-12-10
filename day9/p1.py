
from itertools import batched

data = list(map(int, open("input.txt").read()))


class Node:
    def __init__(self, data: int | None):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def insertHead(self, data: int | None) -> None:
        n = Node(data)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def iterForward(self):
        n = self.head
        while n:
            yield n
            n = n.next

    def getNextSpace(self):
        n = self.head
        while n:
            if n.data == None:
                yield n
            n = n.next

    def getNextFile(self):
        n = self.tail
        while n:
            if n.data != None:
                return n
            n = n.prev

    def iterReverse(self):
        n = self.tail
        while n:
            yield n
            n = n.prev

    def addFile(self, id: int, length: int) -> None:
        for i in range(length):
            self.insertHead(id)

    def addSpace(self, length: int) -> None:
        for i in range(length):
            self.insertHead(None)

    def move(self, s: Node, f: Node) -> None:
        # edgecase
        if s.next == f:
            pass

        # s.data, f.data = f.data, s.data

        if f.prev:
            f.prev.next = None
            self.tail = f.prev

        f.prev = s.prev
        f.next = s.next

        if s.prev:
            s.prev.next = f

        if s.next:
            s.next.prev = f

    def print(self) -> None:
        p = []
        n = self.head
        while (n):
            p.append(n.data)
            n = n.next
        print(p)

    def checksum(self) -> int:
        res = 0
        for i, n in enumerate(self.iterForward()):
            if n.data:
                res += i*n.data
        return res


ll = LinkedList()
id, r = divmod(len(data), 2)

# odd
if r == 1:
    ll.addFile(id, data.pop())

for s, f in batched(reversed(data), 2):
    id -= 1
    ll.addSpace(s)
    ll.addFile(id, f)

for i, s in enumerate(ll.getNextSpace()):
    f = ll.getNextFile()
    if not f or f.next == s:
        break
    ll.move(s, f)


print(ll.checksum())
