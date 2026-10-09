class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        target_index = -1
        
        # Find first occurrence index
        for i in range(len(word)):
            if word[i] == ch:
                target_index = i
                break
                
        # If the character is not found, return the original string
        if target_index == -1:
            return word
            
        s_list = list(word)
        left = 0
        right = target_index
        
        # Reverse from start up to target_index
        while left < right:
            temp = s_list[left]
            s_list[left] = s_list[right]
            s_list[right] = temp
            left = left + 1
            right = right - 1
            
        ans = ""
        for c in s_list:
            ans = ans + c
        return ans