class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid= (l+r)//2
            print("nums mid: ", nums[mid])
            
            if nums[mid] > nums[-1]:
                l = mid+1
                print("nums[l]:", nums[l])
            else:
                r=mid
                print("nums[r]:", nums[r])
        return nums[l]
        