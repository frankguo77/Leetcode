class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
            
        while headB:
            if headB in s:
                return headB
            headB = headB.next
            
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA