class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hash maps need to be utilized 
        s_count={}
        t_count={}

        for char in s: 
            if char in s_count:
                s_count[char] = s_count[char] + 1  #if the char is in the set
            else:
                s_count[char] = 1  # first time seeing it


        for char in t:
            if char in t_count:
                t_count[char] = t_count[char] + 1
            else: 
                t_count[char] =  1

        if t_count==s_count:
            return True
        else:
            return False