from calculate import calculate


def test_calculate_five_plus_six():
    assert calculate("5 + 6") == 11


def test_calculate_three_plus_two():
    assert calculate("3 + 2") == 5


def test_calculate_thirteen_plus_eleven():
    assert calculate("13 + 11") == 24


def test_calculate_five_minus_3_equals_two():
    assert calculate("5 - 3") == 2
   
