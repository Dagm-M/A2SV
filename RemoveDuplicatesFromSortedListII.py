# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-200)
        dummy.next = head
        temp = dummy
        tempBefore = dummy
        tempBB = dummy
        wasDuplicate = False

        while temp != None:
            
            
            if temp.val == tempBefore.val:
                tempBefore.next = temp.next
                wasDuplicate = True
                
            else:
                if wasDuplicate:
                    wasDuplicate = False
                    tempBB.next = temp
                else:
                    tempBB = tempBefore

                tempBefore = temp

            temp = temp.next

        if wasDuplicate:
            tempBB.next = None

        return dummy.next
