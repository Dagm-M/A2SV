# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # fast = head
        # slow = None
        # first = True

        # while fast != None and fast != slow:
        #     if first:
        #         first = False
        #         slow = head
        #     fast = fast.next
        #     if fast == None:
        #         return None
        #     fast = fast.next
        #     slow = slow.next

        # slow = head

        # while fast != None and fast != slow:
        #     fast = fast.next
        #     slow = slow.next

        # return fast

        nodes = set()

        temp = head

        while temp != None:
            nodes.add(temp)
            temp = temp.next
            if temp in nodes:
                return temp

        return None
