class Solution:

  def validPalindrome(self, s: str) -> bool:
    # Helper to check if a specific slice is already a palindrome
    def is_pali(l, r):
      while l < r:
        if s[l] != s[r]:
          return False
        l += 1
        r -= 1
      return True

    left = 0
    right = len(s) - 1

    while left < right:
      if s[left] == s[right]:
        left += 1
        right -= 1
      else:
        # First mismatch: try skipping left OR skipping right
        return is_pali(left + 1, right) or is_pali(left, right - 1)

    return True