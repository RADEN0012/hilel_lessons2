a = [12, 3, 4, 10]
if len(a) > 1:
    last = a[-1]
    i = len(a) - 1
    while i > 0:
        a[i] = a[i - 1]
        i = i - 1
    a[0] = last
print([12, 3, 4, 10], "=>", a)