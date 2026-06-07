# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head == None:
        #     return head
        # node =  ListNode(head.val, None)
        # new_next_node = node
        # while head.next != None:
        #     next_node = head.next
        #     new_next_node =  ListNode(next_node.val, node)
        #     head = next_node
        #     node = new_next_node
        
        # return new_next_node

        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next= prev
            prev = curr
            curr = next_node
        return prev
            
        