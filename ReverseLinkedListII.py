# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head
        values = []

        for i in range(1,right + 1):
            if i >= left:
                values.append(temp.val)
            temp = temp.next

        values.reverse()

        temp = head
        j = 0
        for i in range(1,right + 1):
            if i >= left:
                temp.val = values[j]
                j += 1
            temp = temp.next

        return head
