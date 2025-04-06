
# pytest
import pytest

# BoxExt
from boxext import *




def test_box_from_str():
    # Test with string keys and values
    a = box_from_str("a b c", "1 2 3")
    assert a.a == "1"
    assert a.b == "2"
    assert a.c == "3"

    # Test with list keys and values
    a = box_from_str(["a", "b", "c"], [1, 2, 3])
    assert a.a == 1
    assert a.b == 2
    assert a.c == 3


    # Test with list keys and string values
    a = box_from_str(["a", "b", "c"], "1 2 3")
    assert a.a == "1"
    assert a.b == "2"
    assert a.c == "3"


    # Test with tuple keys and values
    a = box_from_str(("a", "b", "c"), (1, 2, 3))
    assert a.a == 1
    assert a.b == 2
    assert a.c == 3

    # Test with dictionary keys and values
    a = box_from_str({"a":10, "b":20}, {1: 2, 3: 4})
    assert a.a == 2
    assert a.b == 4

    # Test with mixed types
    a = box_from_str("a b c", {1: 2, 3: 4, 5: 6})
    assert a.a == 2
    assert a.b == 4
    assert a.c == 6

    # Test with empty keys and values
    a = box_from_str("", "")
    assert len(a) == 0

    # Test with unequal lengths
    with pytest.raises(ValueError):
        box_from_str("a b c", "1 2")

    with pytest.raises(ValueError):
        box_from_str("a b c", [1, 2])

    with pytest.raises(ValueError):
        box_from_str("a b c", (1, 2))

    with pytest.raises(ValueError):
        box_from_str("a b c", {1: 2, 3: 4})

    with pytest.raises(ValueError):
        box_from_str(["a", "b", "c"], {1: 2, 3: 4})

    with pytest.raises(ValueError):
        box_from_str({'a':10, 'b':20}, {1: 2})

    # Test with Box
    a = box_from_str(Box({"a": 1, "b": 2, "c": 3}), (10,20,30))
    assert a.a == 10
    assert a.b == 20
    assert a.c == 30
    assert isinstance(a, Box)

    a = box_from_str(Box({"a": 1, "b": 2, "c": 3}), Box({"a": 10, "b": 20, "c": 30}))
    assert a.a == 10
    assert a.b == 20
    assert a.c == 30
    assert isinstance(a, Box)


def test_dict_from_str():
    a = dict_from_str("a b c", "1 2 3")
    assert a['a'] == "1"
    assert a['b'] == "2"
    assert a['c'] == "3"

    a = dict_from_str(["a", "b", "c"], [1, 2, 3])
    assert a['a'] == 1
    assert a['b'] == 2
    assert a['c'] == 3

    a = dict_from_str(["a", "b", "c"], "1 2 3")
    assert a['a'] == "1"
    assert a['b'] == "2"
    assert a['c'] == "3"

    a = dict_from_str(("a", "b", "c"), (1, 2, 3))
    assert a['a'] == 1
    assert a['b'] == 2
    assert a['c'] == 3

    a = dict_from_str({"a":10, "b":20}, {1: 2, 3: 4})
    assert a['a'] == 2
    assert a['b'] == 4
    a = dict_from_str("a b c", {1: 2, 3: 4, 5: 6})
    assert a['a'] == 2
    assert a['b'] == 4
    assert a['c'] == 6

    a = dict_from_str("", "")
    assert len(a) == 0

    with pytest.raises(ValueError):
        dict_from_str("a b c", "1 2")
    with pytest.raises(ValueError):
        dict_from_str("a b c", [1, 2])
    with pytest.raises(ValueError):
        dict_from_str("a b c", (1, 2))
    with pytest.raises(ValueError):
        dict_from_str("a b c", {1: 2, 3: 4})
    with pytest.raises(ValueError):
        dict_from_str(["a", "b", "c"], {1: 2, 3: 4})
    with pytest.raises(ValueError):
        dict_from_str({'a':10, 'b':20}, {1: 2})

    a = dict_from_str(Box({"a": 1, "b": 2, "c": 3}), (10,20,30))
    assert a['a'] == 10
    assert a['b'] == 20
    assert a['c'] == 30
    assert isinstance(a, dict)

    a = dict_from_str(Box({"a": 1, "b": 2, "c": 3}), Box({"a": 10, "b": 20, "c": 30}))
    assert a['a'] == 10
    assert a['b'] == 20
    assert a['c'] == 30
    assert isinstance(a, dict)





