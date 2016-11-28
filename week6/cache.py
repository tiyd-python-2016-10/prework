class Cache:
    def __init__(self):
        self.dict = {}

    def get(self, key):
        return self.dict.get(key)

    def set(self, key, value):
        self.dict[key] = value

    def clear(self):
        self.dict = {}

    def has_key(self, key):
        return key in self.dict

    #this allows use of the "in" keyword
    def __contains__(self, key):
        return key in self.dict

    #this is one way to make a collection iterable
    def __iter__(self):
        #use yield for each value, or return an iter object.
        for key, value in self.dict.items():
            yield key, value
#        return iter(self.dict.items())

    def __len__(self):
        return len(self.dict)
