# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         temp = head
#         dummy = None

#         if head == None:
#             return None


#         while temp != None:
#             if dummy == None:
#                 temp2 = ListNode(temp.val,None)
#                 dummy = temp2
#             else:
#                 temp3 = ListNode(temp.val,None)
#                 temp2.next = temp3
#                 temp2 = temp2.next

#             temp = temp.next
#             if temp == None:
#                 break
#             temp = temp.next


#         temp = head.next

#         while temp != None:

#             temp3 = ListNode(temp.val,None)
#             temp2.next = temp3
#             temp2 = temp2.next

#             temp = temp.next
#             if temp == None:
#                 break
#             temp = temp.next

#         return dummy

        if head == None:
            return head
        elif head.next == None:
            return head

        odd = head
        even = head.next

        tempOdd = odd
        tempEven = even

        while tempOdd != None:
            tempOdd.next = tempEven.next

            if tempOdd.next == None:
                break

            tempOdd = tempOdd.next

            tempEven.next = tempOdd.next

            if tempEven.next == None:
                break

            tempEven = tempEven.next

        tempOdd.next = even

        return head   

        
