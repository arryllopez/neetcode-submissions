class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window appraoch 

        # z x y z 
        left = 0 
        maxCount = 0 
        seen = set() 

        for right in range(len(s)): 
            while s[right] in seen: 
                seen.remove(s[left]) 
                left +=1 
            seen.add(s[right])
            maxCount = max (maxCount, right - left + 1)
        
        return maxCount
                
     
