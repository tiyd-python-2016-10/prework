class Sample:
    def __init__(self, name, data=[]):
        if data == None:
            data = []
        self.name = name
        self.data = data

    def add_stuff(self, stuff):
        self.data.append(stuff)
    

    def __str__(self):
        return "{}: {}".format(self.name, str(self.data))


def test_s1():
    s1 = Sample("s1")
    s1.add_stuff("Hi")
    s1.add_stuff("Mom")
    s1.add_stuff("Mac n Cheese")
    print(s1)

def test_s1_again():
    print(s1)

def test_s2():
    s2 = Sample("s2")
    s2.add_stuff("weird")
    print(s2)

if __name__ == "__main__":
    test_s1()
#    test_s1_again()
    test_s2()


