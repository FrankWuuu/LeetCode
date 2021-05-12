# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#                 :type nums: List[int]
#                 :type val: int
#                 :rtype: int
#                 """
#         l = len(nums)
#         temp =[]
#         for i in range(l):
#             if nums[i] != val:
#                 temp.append(nums[i])
#         return temp

class Solution():
    def removeElement(self, nums, val):
        l = len(nums)
        m = n = 0
        while n < l:
            if nums[n] != val:
                nums[m] = nums[n]
                m += 1
            n += 1
        return nums
s = Solution()
nums = [1, 2, 3, 1, 3, 4, 2, 6, 1, 8]
val = 2
ss = s.removeElement(nums, val)
print(ss)
