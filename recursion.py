def fibonnaci(n):
    if n == 1: #base case
        return 1
    if n == 0: #base case
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(6))