# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #creating two pointers to interate through linked list
        prev, curr = None, head

       #iterating through linked list
        while curr:
        #creating a pointer to hold the value that gets lost when assigning curr.next to prev
            nxt = curr.next
            #setting curr.next to point at prev
            curr.next = prev
            #updating prev to be curr
            prev = curr
            #updating curr to be nxt
            curr = nxt
        return prev