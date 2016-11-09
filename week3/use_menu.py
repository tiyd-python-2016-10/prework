from menu import Menu

def login():
    pass
    #do login stuff.

def add():
    pass

m = Menu(quit=True)

m.register("login", login)
m.register("add", add)
m.register("quit", exit)


n = Menu()
n.register("hit", hit)
n.register("stay", stay)
n.register("fold", fold)

o = Menu()
o.register("level", level)


m.display()

# login
# add
# which of the above options would you like to do >
#    if the user chooses login, call login function.
#    if the user chooses add, call add function.
