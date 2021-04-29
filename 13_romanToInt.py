class Solution():
    def romanToInt(self, s):
        temp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)-1):
            if temp[s[i]] < temp[s[i+1]]:
                total = total - temp[s[i]]
            else:
                total = total + temp[s[i]]
        total = total + temp[s[len(s)-1]]
        return total

s = Solution()
ss = s.romanToInt('VMMM')
print(ss)
