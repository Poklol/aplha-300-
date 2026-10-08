class Solution:

  def reverseOnlyLetters(self, s: str) -> str:
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
      # Skip until 'left' lands on an alphabet character
      if not chars[left].isalpha():
        left += 1
      # Skip until 'right' lands on an alphabet character
      elif not chars[right].isalpha():
        right -= 1
      else:
        # Both are letters, swap them!
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)