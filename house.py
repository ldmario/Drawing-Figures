from math import floor

n = int(input())

if n % 2 == 0:
    stars = 2
else:
    stars = 1

dashes = (n - stars) // 2

for row in range(floor((n + 1) / 2)):
    print("-" * dashes, end="")
    print("*" * stars, end='')
    print("-" * dashes)
    stars += 2
    dashes -= 1

for _ in range(n // 2):
    print("|", end="")
    print("*" * (n - 2), end='')
    print("|")
