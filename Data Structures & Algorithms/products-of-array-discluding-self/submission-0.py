class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1] * (len(nums))
        prefix=[1] * (len(nums))
        postfix=[1] * (len(nums))

        for i in range(len(nums)):
            if i ==0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1]* nums[i]

        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                postfix[j] = nums[j]
            else:
                postfix[j]= postfix[j+1] * nums[j]
        
        #print(postfix)
        for i in range(len(nums)):
            if i==0:
                output[i]= 1 * postfix[i+1]
                
            elif i==len(nums) -1:
                output[i]= prefix[i-1] * 1
            else:
                output[i]= prefix[i-1] * postfix[i+1]
        return output        
            
        


        

       