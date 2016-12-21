from stack import *
from nose.tools import raises

def test_default_capacity():
    s = Stack()
    assert s.capacity == None


def test_set_capacity():
    cap = 10
    s = Stack(capacity=cap)
    assert s.capacity == cap

   
def test_push_pop():
    s = Stack()
    s.push(5)
    assert s.pop() == 5


def test_len():
    s = Stack()
    assert len(s) == 0


def test_push_two():
    s = Stack()
    s.push(5)
    s.push(6)
    assert len(s) == 2
    assert s.pop() == 6
    assert len(s) == 1
    assert s.pop() == 5
    assert len(s) == 0


def test_is_empty():
    s = Stack()
    assert s.is_empty()
    s.push("hi")
    assert not s.is_empty()
    s.pop()
    assert s.is_empty()


def test_peek():
    s = Stack()
    s.push("Hi")
    assert s.peek() == "Hi"
    s.push("Mom")
    assert s.peek() == "Mom"
    s.push("Yo")
    assert s.peek() == "Yo"
    assert len(s) == 3
    

@raises StackOutOfBoundsException
def test_empty_peek():
    s = Stack()
    s.peek()



#capacity
#peek()
#find()
