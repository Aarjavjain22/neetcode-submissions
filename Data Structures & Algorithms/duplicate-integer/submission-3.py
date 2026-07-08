class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        S = set()

        for num in nums:
            if num in S:
                return True
            else:
                S.add(num)
        return False
        

        