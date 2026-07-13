class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i=0
        j=len(height)-1
        leftmax=height[i]
        rightmax=height[j]
        answer=0

        while i<j:
            if leftmax <rightmax:
                i+=1
                leftmax= max(leftmax,height[i])
                answer+= leftmax-height[i]
            else:
                j-=1
                rightmax=max(rightmax,height[j])
                answer+= rightmax-height[j]
        return answer


        

          