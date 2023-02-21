# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:
            return head

        dummy = ListNode(-6000,head)

        tempBefore = dummy
        temp = head

        while temp != None:
            temp1Before = dummy
            temp1 = dummy

            while temp1 != None:

                if temp1 == temp:
                    break

                if temp1.val > temp.val:
                    
                    tempBefore.next = temp.next
                    temp1Before.next = temp
                    temp.next = temp1
                    temp = tempBefore

                    break

                temp1Before = temp1
                temp1 = temp1.next

            tempBefore = temp
            temp = temp.next


        return dummy.next        
