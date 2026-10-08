class Solution:

  def countSubstrings(self, s: str) -> int:
    total_palindromes = 0

    # Helper function: expand outward as long as it's a valid palindrome
    def expand_from_center(left, right):
      count = 0
      while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
      return count

    for i in range(len(s)):
      # Odd length palindromes: center is at s[i]
      total_palindromes += expand_from_center(i, i)

      # Even length palindromes: center is between s[i] and s[i+1]
      total_palindromes += expand_from_center(i, i + 1)

    return total_palindromes