class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        left = 0
        right = len(s_list) - 1
        
        # String or set of vowels to check against
        vowels = "aeiouAEIOU"
        
        while left < right:
            # Move left forward if it's not a vowel
            while left < right and s_list[left] not in vowels:
                left = left + 1
                
            # Move right backward if it's not a vowel
            while left < right and s_list[right] not in vowels:
                right = right - 1
                
            # Swap the two vowels
            temp = s_list[left]
            s_list[left] = s_list[right]
            s_list[right] = temp
            
            left = left + 1
            right = right - 1
            
        ans = ""
        for ch in s_list:
            ans = ans + ch
        return ans