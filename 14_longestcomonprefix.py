# -*- coding:utf-8 -*-
class Solution():
    def lcp(self, str1, str2):
        length = min(len(str1),len(str2))
        index = 0
        while index < length and str2[index] == str1[index]:
            index += 1
        return str1[:index]

    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        count = len(strs)
        for i in range(count):
            prefix = self.lcp(prefix, strs[i])  # key point
        return prefix

s = Solution()
ss = s.longestCommonPrefix(['hellowbaby', 'hello world', 'hellowyou', 'hellowkitty'])
print(ss)
