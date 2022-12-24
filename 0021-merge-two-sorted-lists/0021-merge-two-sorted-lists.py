# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not(l1) and not(l2)):
            return None
        if(not(l1)): 
            return l2
        if(not(l2)): 
            return l1
        
        head = ListNode()
        p = head
        
        
        while(l1 and l2):
            if(l1.val <= l2.val):
                p.next = l1
                l1 = l1.next
                p = p.next
                p.next = None   
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
                p.next = None

        if(not(l1)):
            p.next = l2
        
        if(not(l2)):
            p.next = l1
        
    
        return head.next