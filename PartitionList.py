# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        temp = head
        tempBefore = dummy

        while temp != None and temp.val < x:
            tempBefore = temp
            temp = temp.next

        iterator = temp
        
        while iterator != None:
            iteratorBefore = iterator
            iterator = iterator.next

            while iterator != None and iterator.val < x:
                iteratorBefore.next = iterator.next
                tempBefore.next = iterator
                iterator.next = temp
                tempBefore = iterator
                iterator = iteratorBefore.next



        return dummy.next
