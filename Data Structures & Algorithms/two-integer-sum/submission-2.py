class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {} 
        answer = []

        for i in range(len(nums)): 
            differenceNum = target-nums[i] 
            # if difference already iterated over
            if differenceNum in difference:
                answer.append(difference[differenceNum])
                answer.append(i)
                
            #store index of the number
            difference[nums[i]] = i 

        return answer



    