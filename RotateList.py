# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        size = 0
        temp = head

        if k < 1:
            return head

        while temp != None:
            temp = temp.next
            size += 1

        if size < 2:
            return head

        k = k % size
        temp = head
        temp2 = head

        if k == 0:
            return head

        for i in range(size - k):
            temp2 = temp
            temp = temp.next

        temp3 = temp

        while temp != None and temp.next != None:
            temp = temp.next

        temp2.next = None
        temp.next = head
        head = temp3

        return head
