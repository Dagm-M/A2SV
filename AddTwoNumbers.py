# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp1 = l1
        temp2 = l2

        num1 = 0
        num2 = 0
        multiplayer = 1

        while temp1 != None:
            num1 += temp1.val * multiplayer
            multiplayer *= 10
            temp1 = temp1.next

        multiplayer = 1
        while temp2 != None:
            num2 += temp2.val * multiplayer
            multiplayer *= 10
            temp2 = temp2.next

        num3 = num1 + num2
        dummy = ListNode()
        temp = dummy

        while True:
            rem = num3 % 10
            num3 = num3//10
            temp2 = ListNode(rem)
            temp.next = temp2
            temp = temp.next
            if num3 == 0:
                break

        return dummy.next
