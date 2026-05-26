class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array called count, for each strings in list, count characters from a-z of each word
        # eat has 1 e 1 a 1t tea has 1 e 1 a 1 t
        # use a hashmap with the key being the count of characters of each word
        # then the value of the hashmap will be which strings have that specific count
        # """ [1e 1a 1t: tea, ate, eat] """ 
        res = defaultdict(list) # mapping character count of each string to list of anagrams 

        for s in strs: 
            count = [0] * 26 #1 for each character
            for c in s: 
                count[ord(c) - ord("a")] += 1 

            res[tuple(count)].append(s) 

        return list(res.values())