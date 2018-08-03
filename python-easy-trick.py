-- 876. Middle of the Linked List
-- Solution 2
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head

