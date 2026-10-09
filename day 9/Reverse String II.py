class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert to list because Python strings cannot be changed directly
        s_list = list(s)
        n = len(s_list)
        
        # Step through the string jumping 2*k each time
        i = 0
        while i < n:
            left = i
            # Make sure the right pointer doesn't go past the end of the string
            if i + k - 1 < n:
                right = i + k - 1
            else:
                right = n - 1
            
            # Standard two-pointer swap
            while left < right:
                temp = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = temp
                left = left + 1
                right = right - 1
            
            # Jump by 2 * k
            i = i + 2 * k
            
        # Rebuild string
        ans = ""
        for ch in s_list:
            ans = ans + ch
        return ans