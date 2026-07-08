class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S=set()
        i=0
        for num in nums:
            if num in S:
                return True
            else: 
                S.add(num)
        return False