def find_outlier(a):
    if a[0] % 2 != a[1] % 2:
        return a[0] if a[2] % 2 == a[1] % 2 else a[1]
    for i in a:
        if i % 2 != a[0] % 2:
            return i