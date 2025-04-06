
from box import Box
# allowed types for keys and values
#    (str|list|tuple|dict) -> (str|list|tuple|dict)
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


