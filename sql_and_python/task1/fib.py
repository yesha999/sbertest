def fib_row(n=100):
    row = [1, 1]
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        row.append(fib2)
    return row
