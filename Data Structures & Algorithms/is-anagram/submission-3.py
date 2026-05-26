class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cant be anagram if not same length 
        # friend | frienddddd
        if len(s) != len(t): 
            return False 

        # store all seen characters in each word in a hashset
        # note that frequency is also needed so we can use a hashmap 
        # {a : 2} {a:2} 
        seenS = {}
        seenT = {}

        # iterate thru each one and if they are equal sets at the end its an  anagram
        for char in s:
            if char in seenS: 
                seenS[char] += 1 
            else: 
                seenS[char] = 1
        
        for char in t: 
            if char in seenT: 
                seenT[char] += 1 
            else: 
                seenT[char] = 1

        #compate sets
        if seenS == seenT : 
            return True
        
        return False
 
