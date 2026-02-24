import random

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = 0

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def pop_left(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = self.head.next
        self.size -= 1
        return current_head

    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if not current.next:
                    break
                current = current.next
            current.next = new_node
        self.size += 1

    def is_empty(self):
        if not self.head:
            return True
        else:
            return False

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return_str = "Waitlist Status: "
        for node in self:
            return_str = return_str + node.data.first + " " + node.data.last + " -- "
            if not node.next:
                return_str = return_str[:-3] + "\nSize is " + str(self.size)
        return return_str

    def __str__(self):
        return f"{self.head.data.first} {self.head.data.last} ID: {self.head.data.sid} has been moved off the waitlist."
    

class Student:
    def __init__(self, first, last, sid = 0):
        self.first = first
        self.last = last
        self.sid = random.randint(1000000, 9999999) #I had to define here and not in __init__ due to some weird bug with all objects having the same ID.

    def __str__(self):
        if __name__ == '__main__':
            return f"First Name: {self.first}\nLast Name: {self.last}\nStudent ID: {self.sid}\n"
        
waitlist = Queue()
waitlist.add(Student("Mary", "Lamb"))
waitlist.add(Student("Andrew", "Smith"))
waitlist.add(Student("Link", "Zelda"))
linkLength = waitlist.size

for i in range(linkLength):
    print(repr(waitlist))
    print(str(waitlist))
    waitlist.pop_left()
    print("\n")
    if waitlist.is_empty():
        print("Waitlist Status: Empty")
