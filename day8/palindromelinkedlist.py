class Solution:

  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
      return True

    # Step 1: Find the middle using slow and fast pointers
    slow = head
    fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # Step 2: Reverse the second half starting from 'slow'
    prev = None
    curr = slow
    while curr:
      next_temp = curr.next
      curr.next = prev
      prev = curr
      curr = next_temp

    # Step 3: Compare first half and second half
    # 'prev' is now the head of the reversed second half
    left = head
    right = prev
    while right:  # The right half is shorter or equal in length
      if left.val != right.val:
        return False
      left = left.next
      right = right.next

    return True