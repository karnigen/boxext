
from box import Box

# Creates new Box object from keys and values
#  - allowed types for keys and values
#    (str|list|tuple|dict) -> (str|list|tuple|dict)
# Usage:
#   a = box_from_str("a b c", "1 2 3") -> Box(a='1', b='2', c='3')
#   a = box_from_str("a b c", [1, 2, 3]) -> Box(a=1, b=2, c=3)
#   a = box_from_str("a b c", (1, 2, 3)) -> Box(a=1, b=2, c=3)
#   a = box_from_str("a b c", {1: 2, 3: 4, 5: 6}) -> Box(a=2, b=4, c=6)
#   a = box_from_str(["a", "b", "c"], {1: 2, 3: 4, 5: 6}) -> Box(a=2, b=4, c=6)
#   a = box_from_str({'a':10, 'b':20}, {1: 2, 3: 4}) -> Box(a=2, b=4)
#
# Errors on different lengths of keys and values:
#   a = box_from_str("a b c", {1: 2, 3: 4})  - raises ValueError
#   a = box_from_str("a b c", "1 2")  - raises ValueError
#   a = box_from_str("a b c", [1, 2])  - raises ValueError
#   a = box_from_str("a b c", (1, 2))  - raises ValueError
#   a = box_from_str("a b c", {1: 2, 3: 4})  - raises ValueError
def box_from_str(__keys, __values):
    if isinstance(__keys, str):
        __keys = __keys.split()
    elif isinstance(__keys, dict):
        __keys = list(__keys.keys())

    if isinstance(__values, str):
        __values = __values.split()
    elif isinstance(__values, dict):
        __values = list(__values.values())

    if len(__keys) != len(__values):
        raise ValueError("Length of keys and values must be equal")

    return Box(zip(__keys, __values))

def dict_from_str(__keys, __values):
    if isinstance(__keys, str):
        __keys = __keys.split()
    elif isinstance(__keys, dict):
        __keys = list(__keys.keys())

    if isinstance(__values, str):
        __values = __values.split()
    elif isinstance(__values, dict):
        __values = list(__values.values())

    if len(__keys) != len(__values):
        raise ValueError("Length of keys and values must be equal")

    return dict(zip(__keys, __values))



