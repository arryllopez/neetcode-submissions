class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # # s only uppercase
        # # interger k 
        # # choose UP TO k characters of the string and replace
        # # after performing at most k replacements
        # # return length of longest substring contianing ONE character

        # # 

        # # same approach as longest substirng
        # left = 0 
        # countMax = 0 
     
        # seen = {} 
     
       
        # # we find the longest substring with duplciating characters
        # # ensuring that the count of the duplciated characters does not go above k 
        # for right in range(len(s)): 
        #     while s[right] in seen: 
        #         seen.remove(s[left])
        #         left += 1
        #     seen[s[right]] +=1 



                     
        # X Y Y X
        # X in seen
        # Y in seen
        # Y in seen 
        # remove left  

        
        # {A : 4 
        #  B : 3}

        left = 0
        answer = 0
        countMax = 0
        seen = {}

        for right in range(len(s)):
            char = s[right]

            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

            if seen[char] > countMax:
                countMax = seen[char]

            while (right - left + 1) - countMax > k:
                seen[s[left]] -= 1
                left += 1

            currentLength = right - left + 1

            if currentLength > answer:
                answer = currentLength

        return answer