class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        curr = head
        prev = None
        
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
        
        jointosec = prev
        firstReversed = curr
        prev = curr
        curr = curr.next
        right -= 1
            
        while right > 0:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            right -= 1
        
        firstReversed.next = curr
        if jointosec:
            jointosec.next = prev
            return head
        else:     
            return prev
        
