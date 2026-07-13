class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output=[]
        nums.sort()

        for i , a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            
            j=i+1
            k= len(nums)-1
            while j<k:
                x= nums[i] + nums [j] + nums[k]
                if x >0:
                    k -=1
                elif x <0:
                    j+=1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return output
