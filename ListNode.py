# leetcode ListCode 实现
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

class Solution():
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

l1 = [1,2,4]
l2 = [2,3,5]
if isinstance(l1,list):
    l1 = ListNode(l1)
if isinstance(l2, list):
    l2 = ListNode(l2)

if __name__ == "__main__":
    s = Solution()
    ss = s.mergeTwoLists(l1, l2)
    print(ss)
