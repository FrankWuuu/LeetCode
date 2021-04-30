class Solution():
    def isValid(self, s):
        n = len(s)
        if n % 2 != 0:
            return False
        temp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in s:
            if i in temp:
                if stack[-1] != temp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack

s = Solution()
ss = s.isValid('[]{}(){[()]}')
print(ss)
