# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        tempBefore = head

        while temp != None:
            
            if temp.val == tempBefore.val:
                tempBefore.next = temp.next
                
            else:
                tempBefore = temp

            temp = temp.next

        return head
