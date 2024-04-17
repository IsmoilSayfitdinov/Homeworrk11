n = [12, 34, 5, 3, 2, 423, 2, 23, 44]
sum_even = 0
i = 0

while i < len(n):
    if n[i] % 2 == 0:
        sum_even += n[i]
    i += 1

print(sum_even)