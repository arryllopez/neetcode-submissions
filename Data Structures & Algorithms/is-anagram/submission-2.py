class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return true if s and t have the exact same characters and count
        # loop through each string store count and char in a dictionary 
        # compare each dict at the end and true if the same false if not

        if len(s) != len (t):
            return False
        

        countS = {} 
        countT = {} 

        for char in s: 
            # if the char is already in countS 
            if char in countS: 
                # increment value of the char by 1 
                # d : 2 --> d : 3 
                countS[char] +=1
            else: 
                # if not seen before set to 1
                countS[char] = 1 

        for char in t: 
            if char in countT: 
                # increment value of the char by 1 
                # d : 2 --> d : 3 
                countT[char] +=1
            else: 
                # if not seen before set to 1
                countT[char] = 1

        if countT == countS: 
            return True

        return False


