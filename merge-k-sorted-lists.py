# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        def traverse(node):

            while node:
                heappush(heap,node.val)
                node = node.next

        for list in lists:
            traverse(list)

        head = None
        if heap:
            head = ListNode(heappop(heap))
            temp = head

        while heap:
            temp2 = ListNode(heappop(heap))
            temp.next = temp2
            temp = temp2

        return head