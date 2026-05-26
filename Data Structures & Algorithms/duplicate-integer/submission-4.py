class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet = set () #intiializign the hashset containing seen values

        for num in nums: #iterate through array
            if num in seenSet: 
                return True
            #if hasnt been seen in the set
            seenSet.add(num)
        return False