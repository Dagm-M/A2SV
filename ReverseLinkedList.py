# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        temp2 = head
        temp3 = head
        if head == None:
            return head
        elif head.next == None:
            return head
        elif head.next.next == None:
            temp = temp.next
            temp.next = temp2
            temp2.next = None
            return temp

        temp = temp.next.next
        temp2 = temp2.next
        temp3.next = None
        while temp != None:
            temp2.next = temp3
            temp3 = temp2
            temp2 = temp
            temp = temp.next

        temp2.next = temp3

        return temp2
            
