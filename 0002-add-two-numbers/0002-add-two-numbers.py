# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

  def addTwoNumbers(
      self, l1: Optional[ListNode], l2: Optional[ListNode]
  ) -> Optional[ListNode]:
    curr, carry = l1, 0
    while curr:
      val = curr.val + (l2.val if l2 else 0) + carry
      curr.val, carry = val % 10, val // 10

      if not curr.next and (l2 and l2.next or carry):
        curr.next = ListNode(0)

      curr, l2 = curr.next, l2.next if l2 else None
    return l1