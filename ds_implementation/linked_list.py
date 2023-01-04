from command_parser import command_parser


class MyLinkedList(object):
    class Node(object):
        def __init__(self, val=None, Next=None, prev=None):
            self.val = val
            self.next = Next
            self.prev = prev

        def get_data(self):
            return self.val

        def set_data(self, val):
            self.val = val

        def get_next(self):
            return self.next

        def set_next(self, Next):
            self.next = Next

        def get_prev(self):
            return self.prev

        def set_prev(self, prev):
            self.prev = prev

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.length:
            return -1
        current_node = self.head
        for ind in range(index):
            if current_node.next:
                current_node = current_node.get_next()
            else:
                return -1
        return current_node.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_Node = self.Node(val, self.head)
        self.head = new_Node
        if self.tail == None:
            self.tail = new_Node
        self.length += 1

    def printListVals(self):
        current = self.head
        lis = []
        if current:
            for i in range(self.length):
                if current:
                    lis.append(current.val)
                    current = current.next
        print('full list: ', lis, "list length: ", self.length)


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.addAtHead(val)
            return
        new_node = self.Node(val, None, None)
        self.tail.set_next(new_node)
        self.tail = self.tail.get_next()
        self.length += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index < self.length:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = self.Node(val, current.next)
            self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        if self.length > index:
            current_node = self.head
            for ind in range(index - 1):  # getting to the node
                current_node = current_node.get_next()
            if current_node.next == self.tail:
                self.tail = current_node
                current_node.next = None
            else:
                current_node.next = current_node.next.next
            self.length -= 1


def main():
    commands = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    values = [[], [1], [3], [1, 2], [1], [1], [1]]
    output = []
    li = MyLinkedList()
    for num in range(1, len(commands)):
        output.append(command_parser(li, commands[num], values[num]))

    print(output)
    li.printListVals()


if __name__ == "__main__":
    main()
