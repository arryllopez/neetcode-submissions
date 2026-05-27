class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # z x y z x y z 
        # use a set to store if seen 
        seen = set ()
        # increment a counter to indicate length 
        count = 0 
        # pointers
        left = 0 
        
        for i in range(len(s)): 
            while s[i] in seen:
                # z x y z  
                seen.remove(s[left])
                left+=1 
             
            seen.add(s[i])
            # z x y z i is right pointer lef tis left 
            # so if indices left is 4 and indices right is 6
            # thats 4 5 6, 3 substrings, so 6-4 + 1 is 3
            count = max (count, i - left + 1)
        
        return count


         



        