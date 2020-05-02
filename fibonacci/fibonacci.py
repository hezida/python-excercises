def fibonacci(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fibonacci(val-1) + fibonacci(val-2)

print(fibonacci(5))