# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        temp = newHead

        while list1 != None and list2 != None:
            if list1.val > list2.val:
                temp2 = ListNode(list2.val)
                temp.next = temp2
                temp = temp2
                list2 = list2.next
            else:
                temp2 = ListNode(list1.val)
                temp.next = temp2
                temp = temp2
                list1 = list1.next


        while list1 != None:
            temp2 = ListNode(list1.val)
            temp.next = temp2
            temp = temp2
            list1 = list1.next

        while list2 != None:
            temp2 = ListNode(list2.val)
            temp.next = temp2
            temp = temp2
            list2 = list2.next

        newHead = newHead.next

        return newHead
