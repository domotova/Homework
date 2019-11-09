class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def node(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [' +str(current.value) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        if self.first == None:
            self.first.value = x
            self.last.next = None
        else:
            self.last.next = self.first
            self.first.value = x


if __name__ == '__main__':
    L = LinkedList()
    L.add(1)
    L.add(2)
    L.add(3)
    print(L)