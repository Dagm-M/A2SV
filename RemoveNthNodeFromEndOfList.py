# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0

        while temp != None:
            temp = temp.next
            size += 1
            
        if size == 1:
            return None
        elif n == size:
            return head.next

        temp = head
        tempBefore = head
        for i in range(size - n):
            tempBefore = temp
            temp = temp.next

        tempBefore.next = temp.next


        return head
