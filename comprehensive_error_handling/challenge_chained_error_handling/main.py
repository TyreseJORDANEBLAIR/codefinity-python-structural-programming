def safe_int_divide(a, b):
    try:
        result = a // b
        return result
    except ZeroDivisionError as e:
        raise ValueError("Cannot divide by zero") from e
    except Exception:
        raise