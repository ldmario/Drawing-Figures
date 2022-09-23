n = int(input())

for row in range(1, n + 1):
    if row < n:
        print(" " * (n - row), end="")
    for col in range(row):
        print("*", end=" ")
    print()
for rows in range(n - 1, 0, -1):
    if rows < n:
        print(" " * (n - rows), end="")
    for col in range(rows):
        print("*", end=" ")
    print()