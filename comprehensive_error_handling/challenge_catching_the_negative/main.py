# Define your custom exception class below
class NegativeNumberError(Exception):
    """Raised when a number is negative."""
    pass

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError("Number must be non-negative")
    return num

try:
    print(check_positive_number(-5))
except NegativeNumberError as e:
    print(e)

print(check_positive_number(3))
print(check_positive_number(0))