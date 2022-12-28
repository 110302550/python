def p09(citations=[1,0,6,5,3]):
    h=None
    # ↓程式區域↓
    a = citations
    a.append(-1)
    a.sort()
    a.reverse()
    for i in range(0,len(a)):
        if a[i] < i+1:
            h = i
            break

    # ↑程式區域↑4

    return h

print(p09())


