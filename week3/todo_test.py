from todo import TodoList

def test_new():
    with open("test.db", "w") as f:
        pass
    with open("test.db") as f:
        assert f.read() == ""


def test_add():
    tl = TodoList("test.db")
    tl.add("Blah")
    assert "Blah" in tl


def test_persist():
    tl = TodoList("test.db")
    assert "Blah" in tl


def test_add_again():
    tl = TodoList("test.db")
    tl.add("di")
    assert "di" in tl


def test_remove():
    tl = TodoList("test.db")
    tl.remove(0)
    assert "Blah" not in tl


def test_remove_persist():
    tl = TodoList("test.db")
    assert "Blah" not in tl


def test_add_persist_2():
    tl = TodoList("test.db")
    assert "di" in tl


def test_clear():
    tl = TodoList("test.db")
    tl.clear()
    with open("test.db") as f:
        assert f.read() == ""
