class OddList():
    def __init__(self, internal_list):
        self.internal_list = internal_list

    def append(self, new_element):
        self.internal_list.append(new_element)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.internal_list[self.index]

    def __getitem__(self, index1):
        return self.internal_list[index1]
