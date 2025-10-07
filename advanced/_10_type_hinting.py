def add(a: int, b: int) -> int:
    return a + b


# run mypy to check type hints. This will raise an error because of incompatible types
# mypy advanced/_10_type_hinting.py
print(add(1, 2.2))
