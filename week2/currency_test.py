from currency import Currency

def test_add_two_currencies():
    one_dollar = Currency('USD', 1)
    two_dollars = Currency('USD', 2)
    result = one_dollar + two_dollars
    assert result.value == 3
    assert result.currency_type == 'USD'
    assert isinstance(result, Currency)
