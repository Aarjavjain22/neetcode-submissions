class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        dict1={}
        for num in nums:
            r= target - num

            if r in dict1:
                return [dict1[r],i]
            else:
                dict1[num]=i
            i+=1
        