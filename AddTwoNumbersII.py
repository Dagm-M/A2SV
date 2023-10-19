# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        while l1:
            s1 += str(l1.val)
            l1 = l1.next

        s2 = ""
        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        i, j = len(s1) - 1, len(s2) - 1
        extra = 0
        s3 = ""
        while i >= 0 or j >= 0:
            if i < 0:
                temp = int(s2[j]) + extra
                if temp > 9:
                    extra = temp // 10
                    temp %= 10
                else:
                    extra = 0
                s3 += str(temp)
            elif j < 0:
                temp = int(s1[i]) + extra
                if temp > 9:
                    extra = temp // 10
                    temp %= 10
                else:
                    extra = 0
                s3 += str(temp)
            else:
                temp = int(s1[i]) + int(s2[j]) + extra
                if temp > 9:
                    extra = temp // 10
                    temp %= 10
                else:
                    extra = 0
                s3 += str(temp)
            i -= 1
            j -= 1

        start = None
        prev = None
        if extra > 0:
            temp = ListNode(extra)
            start = temp
            prev = temp

        for digit in reversed(s3):
            if start is None:
                temp = ListNode(int(digit))
                start = temp
                prev = temp
            else:
                temp = ListNode(int(digit))
                prev.next = temp
                prev = temp

        return start

        
