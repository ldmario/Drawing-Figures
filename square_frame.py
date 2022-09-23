n = int(input())

print("+", end=" ")
for _ in range(n - 2):
    print("-", end=" ")
print("+", end=" ")
print()
for _ in range(n -2):
    print("|", end=" ")
    for _ in range(n - 2):
        print("-", end=" ")
    print("|", end=" ")
    print()
print("+", end=" ")
for _ in range(n - 2):
    print("-", end=" ")
print("+", end=" ")