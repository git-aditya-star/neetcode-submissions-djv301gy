# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # s = set()
        # while head:
        #     if head in s:
        #         return True
        #     s.add(head)
        #     head = head.next
        # return False
        if head is None:
            return False
        
        slow = head
        if  slow.next != slow:
            fast = slow.next
        else:
            return True

        while fast:
            if slow == fast :
                return True
            slow = slow.next
            try :
                fast = fast.next.next
            except Exception as e:
                return False
        return False


