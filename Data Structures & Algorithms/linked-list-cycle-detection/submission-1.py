# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Traverse the linked list with fast slow pointer where slow pointer will moved by one and fast pointer will move by 2

In any case if slow == fast then, it is cycle 

In any case slow is None then it is not cycle

return bool
'''


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        #bool isCycle = false

        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                break 
                
        return False
        '''
        slow = head
        while slow is not None:
            slow = slow.next
            fast = fast.next

            if slow == fast:
                return 
        '''
        

