class Solution:

  def isPalindrome(self, x: int) -> bool:
    # Negative numbers or numbers ending in 0 (except 0 itself) can't be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
      return False

    reversed_half = 0

    # Pop digits from x and push onto reversed_half until we reach the middle
    while x > reversed_half:
      last_digit = x % 10
      reversed_half = (reversed_half * 10) + last_digit
      x //= 10

    # For even-digit numbers: x == reversed_half (e.g., 1221 -> x = 12, reversed_half = 12)
    # For odd-digit numbers:  x == reversed_half // 10 (e.g., 12321 -> x = 12, reversed_half = 123)
    return x == reversed_half or x == (reversed_half // 10)