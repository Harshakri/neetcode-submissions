# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     creating 2 pointers to point at curr and prev
        prev, curr = None, head
    
    #iterating through curr till it hits None:
        while curr:
            #creating a pointer to point at curr.next which will be lost when setting curr.next to prev
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    