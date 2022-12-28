def p02(a=1, b=100):
    evensum=None
    # ↓程式區域↓
    a = input()
    b = input()
    evensum = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            evensum += i
    # ↑程式區域↑
    return evensum