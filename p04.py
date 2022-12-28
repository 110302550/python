def p04(input=25):
    output_list=None
    # ↓程式區域↓
    output_list = ['']
    if input == None:
        output_list = []
    else:
        for i in str(input):
            front = (int(i)-2)*3+97
            if (int(i)>=8):
                front += 1
            end = front + 3
            if (i == '7' or i == '9'):
                end += 1
            temp = output_list
            output_list = []
            for t in temp:
                for y in range(front,end):
                    output_list.append(t + chr(y))
    # ↑程式區域↑
    return output_list

print(p04())