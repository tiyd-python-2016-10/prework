#!/usr/bin/env python3
from sys import argv


class TodoList:
    def __init__(self, data_filename="tasks.db"):
        self.data_filename = data_filename
        self.tasks = []
        with open(self.data_filename, "r") as f:
            for line in f:
                self.tasks.append(line.strip())

    def __getitem__(self, index):
        return self.tasks[index]

    def add(self, new_task):
        self.tasks.append(new_task)
        self._save()

    def remove(self, index):
        try:
            index = int(index)
        except:
            pass
        if isinstance(index, int):
            self.tasks.pop(index)
        else:
            if index in self.tasks:
                self.tasks.pop(self.tasks.index(index))
        self._save()

    def clear(self):
        self.tasks = []
        self._save()

    def _save(self):
        with open(self.data_filename, "w") as f:
            for task in self.tasks:
                f.write(task)
                f.write("\n")


def main():
    tl = TodoList()

    if "--list" in argv:
        for number, task in enumerate(tl):
            print(number, task)
        exit()

    if "--add" in argv:
        tl.add(" ".join(argv[argv.index("--add") + 1:]))
        exit()

    if "--remove" in argv:
        tl.remove(argv[argv.index("--remove") + 1])
        exit()

if __name__ == "__main__":
    main()
