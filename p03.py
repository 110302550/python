def p03(x=123):
    reverse=None
    # ↓程式區域↓
    a = input()
    a = str(x)
    if a[0] == '-':
        b = a[1:]
        b = b[::-1]
        b = '-' + b
    else:
        b = a[::-1]
    reverse = int(b)
    # ↑程式區域↑
    return reverse