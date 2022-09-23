n = int(input())

for row in range(n + 1):
    if row < n:
        print(" " * (n - row), end="")
    for col in range(row):
        print("*", end="")
    print(" | ", end="")
    for cols in range(row):
        print("*", end="")
    print()
