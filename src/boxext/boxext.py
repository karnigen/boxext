

from box import Box   # install python-box

def zip_keys_values(__keys : (str|list|tuple|dict), __values : (str|list|tuple|dict)) -> iter:
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

    return zip(__keys, __values)



# Creates new Box object from keys and values
#  - allowed types for keys and values
#    (str|list|tuple|dict) -> (str|list|tuple|dict)
# Usage:
#   a = str_box("a b c", "1 2 3") -> Box(a='1', b='2', c='3')
#   a = str_box("a b c", [1, 2, 3]) -> Box(a=1, b=2, c=3)
#   a = str_box("a b c", (1, 2, 3)) -> Box(a=1, b=2, c=3)
#   a = str_box("a b c", {1: 2, 3: 4, 5: 6}) -> Box(a=2, b=4, c=6)
#   a = str_box(["a", "b", "c"], {1: 2, 3: 4, 5: 6}) -> Box(a=2, b=4, c=6)
#   a = str_box({'a':10, 'b':20}, {1: 2, 3: 4}) -> Box(a=2, b=4)
#
# Errors on different lengths of keys and values:
#   a = str_box("a b c", {1: 2, 3: 4})  - raises ValueError
#   a = str_box("a b c", "1 2")  - raises ValueError
#   a = str_box("a b c", [1, 2])  - raises ValueError
#   a = str_box("a b c", (1, 2))  - raises ValueError
#   a = str_box("a b c", {1: 2, 3: 4})  - raises ValueError

def str_box(__keys : (str|list|tuple|dict), __values : (str|list|tuple|dict))  -> Box:
    return Box(zip_keys_values(__keys, __values))

def str_dict(__keys : (str|list|tuple|dict), __values : (str|list|tuple|dict))  -> dict:
    return dict(zip_keys_values(__keys, __values))

# Updates keys and values in the given Box|dict object, prefer __values
# a = str_box("a b c", "1 2 3")
# update_keys_values(a, "b c", "4 5")
def update_pairs(__a: dict, __keys: (str|list|tuple|dict), __values: (str|list|tuple|dict)) -> None:
    __a.update(zip_keys_values(__keys, __values))

# Updates selected keys from __b to __a, prefer __b values
def update_selected(__a: dict, __b: dict, __keys: (str|list|tuple|dict)) -> None:
    if isinstance(__keys, str):
        __keys = __keys.split()
    elif isinstance(__keys, dict):
        __keys = list(__keys.keys())

    for k in __keys:
        if k in __b:
            __a[k] = __b[k]