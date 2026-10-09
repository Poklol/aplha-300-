class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        for w_idx in range(len(words)):
            word_list = list(words[w_idx])
            left = 0
            right = len(word_list) - 1
            
            # Reverse characters of the single word
            while left < right:
                temp = word_list[left]
                word_list[left] = word_list[right]
                word_list[right] = temp
                left = left + 1
                right = right - 1
            
            # Reconstruct the single reversed word
            reversed_word = ""
            for ch in word_list:
                reversed_word = reversed_word + ch
            words[w_idx] = reversed_word
            
        # Combine all words with spaces
        ans = ""
        for i in range(len(words)):
            ans = ans + words[i]
            if i != len(words) - 1:
                ans = ans + " "
        return ans