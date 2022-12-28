def p08(n=12):
    output=None
    # ↓程式區域↓
    def dp(n):
        if(n <= 3):
            output = n
        ans = n
        for i in range(1,n+1):
            temp = i**2
            if(temp > n):
                break
            else:
                ans = min(ans,1+dp(n-temp))
        return ans
    output = dp(n)
    # ↑程式區域↑
    return output