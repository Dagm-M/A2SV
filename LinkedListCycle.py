# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # nodes = set()

        # temp = head

        # while temp != None:
        #     nodes.add(temp)
        #     temp = temp.next
        #     if temp in nodes:
        #         return True

        # return False

        fast = head
        slow = head

        while fast != None:

            fast = fast.next

            if fast == None:
                return False

            fast = fast.next
            slow = slow.next

            if fast == slow:
                return True

        return False


