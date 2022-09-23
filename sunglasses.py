from math import floor

n = int(input())

print("*" * (n * 2), end="")
print(" " * n, end="")
print("*" * (n * 2), end="")
print()
for rows in range(n - 2):
    print("*", end="")
    for _ in range(2 * n - 2):
        print("/", end="")
    print("*", end="")
    if rows == floor((n - 1) / 2 - 1):
        print("|" * n, end="")
    else:
        print(" " * n, end="")
    print("*", end="")
    for _ in range(2 * n - 2):
        print("/", end="")
    print("*", end="")
    print()
print("*" * (n * 2), end="")
print(" " * n, end="")
print("*" * (n * 2), end="")
