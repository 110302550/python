def p06(nums = [2,7,11,15], target = 9):
    output_list=None
    # ↓程式區域↓
    for i in range(0,len(nums)):
        for t in range(0,len(nums)):
            if (i != t and nums[i] + nums[t] == target):
                output_list = [i,t]
    # ↑程式區域↑
    return output_list