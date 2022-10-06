"""
This is a really bad solution I came up with.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    target = result
    p1, p2 = l1, l2
    carry = 0
    while True:
        target.val = (p1.val + p2.val + carry) % 10
        carry = (p1.val + p2.val + carry) // 10
        if p1.next is None and p2.next is None:
            if carry != 0:
                target.next = ListNode(val=carry, next=None)
            break
        if p1.next is None:
            p1 = ListNode(val=0, next=None)
        else:
            p1 = p1.next
        if p2.next is None:
            p2 = ListNode(val=0, next=None)
        else:
            p2 = p2.next
        target.next = ListNode(val=0, next=None)
        target = target.next
    return result
