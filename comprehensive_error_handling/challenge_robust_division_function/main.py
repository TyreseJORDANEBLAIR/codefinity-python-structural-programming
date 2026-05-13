def robust_divide(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            return "Invalid input type"
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Example calls for testing
div1 = robust_divide(10, 2)
div2 = robust_divide(5, 0)
div3 = robust_divide('10', 2)
div4 = robust_divide(8, '0')
div5 = robust_divide(7.5, 2.5)
print(div1, div2, div3, div4, div5)