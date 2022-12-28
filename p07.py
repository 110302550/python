def p07(version1='1.0.0', version2='1.0.0'):
    output=None
    # ↓程式區域↓
    l1 = version1.split('.')
    l2 = version2.split('.')
    for i in range(0,len(l1)):
        l1[i] = int(l1[i])
    for i in range(0,len(l2)):
        l2[i] = int(l2[i])
    output = 0
    if(len(l1) == len(l2)):
        for i in range(0,len(l1)):
            if(l1[i] > l2[i]):
                output = 1
                break
            elif(l1[i] < l2[i]):
                output = -1
                break
    else:
        output = 0
            
    # ↑程式區域↑
    return output