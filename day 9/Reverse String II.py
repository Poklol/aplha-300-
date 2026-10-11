class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        s_list = list(s)
        n = len(s_list)
        
       
        i = 0
        while i < n:
            left = i
           
            if i + k - 1 < n:
                right = i + k - 1
            else:
                right = n - 1
            
           
            while left < right:
                temp = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = temp
                left = left + 1
                right = right - 1
            
           
            i = i + 2 * k
            
        
        ans = ""
        for ch in s_list:
            ans = ans + ch
        return ans
