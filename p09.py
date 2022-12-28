def p09(citations=[]):
    h=None
    # ↓程式區域↓
    h = 0
    while True:
        H = 0
        for i in citations:
            if i >= h:
                H += 1
        if H < h:
            h += 1
            break
        elif H >= h:
            h += 1
    # ↑程式區域↑
    return h