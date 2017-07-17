a = [14, 3, 7, 1, 5, 9, 2, 4]

for j in range(0, len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
        a[i + 1] = a[i]
        i = i - 1
    a[i + 1] = key

print a
