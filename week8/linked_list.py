
#print
#insert
#append
#remove
#find

class Link:
    def __init__(self, data):
        self.data = data
        self.next_link = None
        
    def has_next(self):
        return self.next_link != None

    def next(self):
        return self.next_link

    def set_next(self, link):
        self.next_link = link


class LinkedList:
    def __init__(self):
        self.start = None
        self.size = 0

    def walk_list(self):
        curr = self.start
        while curr.has_next():
            curr = curr.next()
        
    def append(self, data):
        if self.size == 0:
            self.start = Link(data)
            self.size += 1
            return
        self.size += 1
        curr = self.start
        while curr.next_link != None:
            curr = curr.next_link
        curr.next_link = Link(data)

    def insert(self, data, index):
        if index > self.size: raise IndexOutOfBoundsException
        new_link = Link(data)
        self.size += 1
        if index == 0:
            if self.start: new_link.set_next(self.start)
            self.start = new_link
            return
        i = 0
        curr = self.start
        while i < index:
            curr = curr.next()
            i += 1
        
        new_link.set_next(curr.next())
        curr.set_next(new_link)
         

    def __getitem__(self, index):
        if index >= self.size or self.size == 0: raise IndexOutOfBoundsException
        curr = self.start
        i = 0
        curr = self.start
        while i < index:
            curr = curr.next()
            i += 1
        return curr.data

    def __str__(self):
        if self.size == 0: return "[]"
        out = ""
        curr = self.start
        while curr.next_link != None:
            out += str(curr.data) + ", "
            curr = curr.next_link
        return "[" + out + str(curr.data) + "]"


def test():
    #testing link...
    #create link - assert that next is None and Data is data
    #create second link, set it as next for first link...  assert this is true.
    
    ##LL 
    #create linked list.
    #assert size is 0
    #insert something.
    #assert size is 1
    #prove that you can get something out. (or that something is in ll)
    #insert second element
    #assert size is 2
    #assert that elements are in correct order.
   
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert("insert before 0", 0)
    ll.insert("insert at end ", ll.size)
    ll.insert("insert after 1 ", 2)
    print(ll)
    return 
    
    ll = LinkedList()
    ll2 = LinkedList()
    ll2.append(4)
    ll2.append(5)
    ll2.append(6)
    ll2.append(7)
    ll.append("Hi")
    ll.append("Mom")
    ll.append("here")
    ll.append("did this work")
    ll.append(ll2)
    ll.append("another string")
    ll.append("2 ago was a linked list")
    ll.insert("first", 0)
    ll.insert("put me in 2", 2)
    ll.insert("put me at the end", ll.size)
    print(ll)
    print(ll[0])
    print(ll[2])
    print(ll[ll.size - 1])
    print(ll.size)

if __name__ == "__main__":
    test()
