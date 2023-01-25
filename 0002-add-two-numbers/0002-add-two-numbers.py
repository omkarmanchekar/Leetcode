# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ll = ListNode()
        head = ll
        while(l1 != None or l2 != None or carry != 0):
            num1 = 0
            num2 = 0
            if(l1):
                num1 = l1.val
                l1 = l1.next
            if(l2):
                num2 = l2.val
                l2 = l2.next
                
            res = num1 + num2 + carry 
            
            carry = res//10

            
            new_head = ListNode(res%10)
            head.next = new_head
            head = new_head
            

        return ll.next
            
            

        