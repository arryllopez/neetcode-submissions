class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first sort the array so that all same numbers are adjacent
        nums.sort() 
        # [1,1,1,2,2,3,4,4,4,4]

        # to find the k most frequent 
        # count frequencies of all numbers
        seen = {} 
        for num in nums: 
            if num not in seen: 
                seen[num] = 1 
            else: 
                seen[num] += 1 
        
        # {1 : 3 } 
        # {2:2}
        answer = [] 

        sorted_nums = sorted(seen.items(), key = lambda item: item[1], reverse = True)
        # use the kth frequent to find the kth frequent 
        # if k is 2 for example, find the hasmap value greater or equal to 2
        for key, value in sorted_nums[:k]:
            answer.append(key)  
                
        return answer