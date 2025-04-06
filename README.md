## Python-Box: Access Dicts Like Objects

`Python-Box` lets you access dictionaries using attribute-style access (dot notation). It's super handy for working with JSON, configuration files, or any data where you'd prefer `data.key` over `data['key']`.


## Installation

To install `boxext`, use the following command:

```bash
uv tool install --from git+https://github.com/karnigen/boxext boxext
```

To upgrade `boxext`, use the following command:

```bash
uv tool upgrade boxext
```

## Usage

## str_box Function Examples

Here are examples demonstrating the usage of the `str_box` function:

* `a = str_box("a b c", "1 2 3")` -> `Box(a='1', b='2', c='3')`
* `a = str_box("a b c", [1, 2, 3])` -> `Box(a=1, b=2, c=3)`
* `a = str_box("a b c", (1, 2, 3))` -> `Box(a=1, b=2, c=3)`
* `a = str_box("a b c", {1: 2, 3: 4, 5: 6})` -> `Box(a=2, b=4, c=6)`
* `a = str_box(["a", "b", "c"], {1: 2, 3: 4, 5: 6})` -> `Box(a=2, b=4, c=6)`
* `a = str_box({'a':10, 'b':20}, {1: 2, 3: 4})` -> `Box(a=2, b=4)`

## Error Handling

The `str_box` function raises a `ValueError` when the lengths of the keys and values do not match:

* `a = str_box("a b c", {1: 2, 3: 4})` -> raises `ValueError`
* `a = str_box("a b c", "1 2")` -> raises `ValueError`
* `a = str_box("a b c", [1, 2])` -> raises `ValueError`
* `a = str_box("a b c", (1, 2))` -> raises `ValueError`
* `a = str_box("a b c", {1: 2, 3: 4})` -> raises `ValueError`
