class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lL = None
        hL = None
        
        while head:
            if head.val >= x:
                if hL:
                    h.next = head
                else:
                    hL = head
                h = head
            else:
                if lL:
                    l.next = head
                else:
                    lL = head
                l = head
            head = head.next

        if lL:
            l.next = hL
        if hL:
            h.next = None

        return lL or hL