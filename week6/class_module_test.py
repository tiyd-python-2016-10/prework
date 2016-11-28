# import cache
#
#
# def test_get_when_not_set_returns_none():
#     assert cache.get("foo") is None
#
#
# def test_get_when_set_returns_value():
#     cache.set("foo", "bar")
#     assert cache.get("foo") == "bar"
#
#
# def test_clear_empties_cache():
#     cache.set("foo", "bar")
#     cache.clear()
#     assert cache.get("foo") is None
#
#
# def test_has_key_when_not_set_returns_false():
#     cache.clear()
#     assert not cache.has_key("foo")
#
#
# def test_has_key_when_set_returns_true():
#     cache.clear()
#     cache.set("foo", "bar")
#     assert cache.has_key("foo")
#
#
# def test_in_when_not_set_returns_false():
#     cache.clear()
#     assert "foo" not in cache
#
#
# def test_in_when_set_returns_true():
#     cache.clear()
#     cache.set("foo", "bar")
#     assert "foo" in cache
#
#
# def test_iteration():
#     cache.clear()
#     cache.set("foo", "bar")
#     cache.set("baz", "quux")
#     results = []
#     for key, value in sorted(cache):
#         results.append("{}={}".format(key, value))
#     result = ', '.join(results)
#     print(result)
#     assert result == "baz=quux, foo=bar"
#
#
# def test_len():
#     cache.clear()
#     cache.set("foo", "bar")
#     cache.set("baz", "quux")
#     assert len(cache) == 2
#
