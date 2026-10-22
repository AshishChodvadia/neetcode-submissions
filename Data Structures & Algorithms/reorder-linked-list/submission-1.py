# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Base case - only work with lists of 3 or more nodes
        if not head or not head.next or not head.next.next:
            return

        # 1. Find middle of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        back = prev
        front = head

        # 3. Interleave
        while back:
            front_temp = front.next
            back_temp = back.next
            front.next = back
            back.next = front_temp  
            front = front_temp
            back = back_temp     