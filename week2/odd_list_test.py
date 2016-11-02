from odd_list import OddList


def test_create():
    OddList([1,3,5])


def test_append():
    new_element = 5
    new_list = OddList([])
    new_list.append(new_element)
    assert 5 in new_list.internal_list
