## Python-Box: Access Dicts Like Objects

`Python-Box` lets you access dictionaries using attribute-style access (dot notation). It's super handy for working with JSON, configuration files, or any data where you'd prefer `data.key` over `data['key']`.


## Installation

To install `boxext`, use the following command:

```bash
uv add git+https://github.com/karnigen/boxext
```

To uninstall, use the following command:

```bash
uv remove boxex
```

To upgrade `boxext`, use the following command:

```bash
uv sync [-U|--upgrade]
uv sync [-P|--upgrade-package] boxext
```

## Usage

## str_box/str_dict Function Examples

Here are examples demonstrating the usage of the `str_box` function:

**Examples:**


* `a = str_box("a b c", "1 2 3")` -> `Box(a='1', b='2', c='3')`
* `a = str_box("a b c", [1, 2, 3])` -> `Box(a=1, b=2, c=3)`
* `a = str_box("a b c", (1, 2, 3))` -> `Box(a=1, b=2, c=3)`
* `a = str_box("a b c", {1: 2, 3: 4, 5: 6})` -> `Box(a=2, b=4, c=6)`
* `a = str_box(["a", "b", "c"], {1: 2, 3: 4, 5: 6})` -> `Box(a=2, b=4, c=6)`
* `a = str_box({'a':10, 'b':20}, {1: 2, 3: 4})` -> `Box(a=2, b=4)`


## str_dict Function Examples

Here are examples demonstrating the usage of the `str_dict` function:

**Examples:**

* `a = str_dict("a b c", "1 2 3")` -> `{'a': '1', 'b': '2', 'c': '3'}`
* `a = str_dict("a b c", [1, 2, 3])` -> `{'a': 1, 'b': 2, 'c': 3}`
* `a = str_dict("a b c", (1, 2, 3))` -> `{'a': 1, 'b': 2, 'c': 3}`
* `a = str_dict("a b c", {1: 2, 3: 4, 5: 6})` -> `{'a': 2, 'b': 4, 'c': 6}`
* `a = str_dict(["a", "b", "c"], {1: 2, 3: 4, 5: 6})` -> `{'a': 2, 'b': 4, 'c': 6}`
* `a = str_dict({'a':10, 'b':20}, {1: 2, 3: 4})` -> `{'a': 2, 'b': 4}`


## Error Handling

The `str_box` function raises a `ValueError` when the lengths of the keys and values do not match:

**Examples:**

* `a = str_box("a b c", {1: 2, 3: 4})` -> raises `ValueError`
* `a = str_box("a b c", "1 2")` -> raises `ValueError`
* `a = str_box("a b c", [1, 2])` -> raises `ValueError`
* `a = str_box("a b c", (1, 2))` -> raises `ValueError`
* `a = str_box("a b c", {1: 2, 3: 4})` -> raises `ValueError`


## update_pairs Function Examples

Updates keys and values in the given Box or dict object, preferring `values`.

**Examples:**


* `a = str_box("a b c", "1 2 3")`
* `update_pairs(a, "b c", "4 5")` -> `Box(a='1', b='4', c='5')`


## update_selected Function Examples

Updates selected keys in the given Box or dict object from another Box or dict.

**Examples:**

* `a = str_box("a b c", "1 2 3")`
* `b = str_box("b c d", "4 5 6")`
* `update_selected(a, b, "b c")` -> Updates `a` with values from `b` for keys "b" and "c".
* `update_selected(a, b, a)` -> Updates `a` with values from `b` but only for keys present in `a`.

## mget Function Description

`mget` - returns a tuple of values for the specified keys from the input Box or dictionary.

**Examples:**

* `a = str_box("a b c", [1, 2, 3])`
* `mget(a, "a b")` -> `(1, 2)`

* `b = str_box("b c d", [4, 5, 6])`
* `mget(a, b)` -> `(2, 3)` (Returns values from `a` for keys present in `b`)


## mdel Function Description

`mdel` - deletes the specified keys from the input Box or dictionary  and returns a list of the deleted keys. This is particularly useful for determining which keys were actually removed.

**Example:**

* `a = str_box("a b c", [1, 2, 3])`
* `mdel(a, "a b")` -> `['a', 'b']`, resulting in `a` being modified to `{'c': 3}`.


## mset Function Description

`mset` - sets the same value for multiple keys in the input Box or dictionary.

**Examples:**

* `a = Box()`
* `mset(a, "a b c", 1)` -> `a` is now `{'a': 1, 'b': 1, 'c': 1}`

* `mset(a, "a b c", [])` -> `a` is now `{'a': [], 'b': [], 'c': []}`

## mlambda Function Description

`mlambda` - applies a lambda function to specified keys and corresponding values in the input Box or dictionary.

**Examples:**

* `a = Box()`
* `mlambda(a, "a b c", [1,2,3], lambda d, k, v: d.update({k: [v]}))`
    * This will set `a` to `{'a': [1], 'b': [2], 'c': [3]}`.
* `mlambda(a, "a b c", [3,4,5], lambda d, k, v: d[k].append(v))`
    * Assuming `a` is `{'a': [1], 'b': [2], 'c': [3]}` after the previous example, this will append the values, resulting in `{'a': [1, 3], 'b': [2, 4], 'c': [3, 5]}`.