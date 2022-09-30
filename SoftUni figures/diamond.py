from math import floor
n = int(input())

stars = 1
left_or_right_dashes = (n - 1) // 2
mid_dashes = n - 2 * left_or_right_dashes - 2
mid_row = False

for row in range(n):
    if n % 2 == 0 and row == n - 1:
        break
    if row == floor(n / 2) or (n % 2 == 0 and row == floor((n - 1) / 2)):
        mid_row = True

    if row == 0 or row == n - 1:
        if n % 2 == 0:
            print("-" * left_or_right_dashes, end='')
            print("*" * (stars * 2), end='')
            print("-" * left_or_right_dashes)
        else:
            print("-" * left_or_right_dashes, end='')
            print("*" * stars, end='')
            print("-" * left_or_right_dashes)
    else:
        print("-" * left_or_right_dashes, end='')
        print("*" * stars, end='')
        print("-" * mid_dashes, end='')
        print("*" * stars, end='')
        print("-" * left_or_right_dashes)
    if mid_row:
        left_or_right_dashes += 1
        mid_dashes -= 2
    elif not mid_row:
        left_or_right_dashes -= 1
        mid_dashes += 2
