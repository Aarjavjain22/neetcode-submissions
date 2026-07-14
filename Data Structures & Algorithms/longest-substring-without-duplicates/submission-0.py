class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set=set()
        i=0
        j=0
        maxlength=0
        for j in range(len(s)):
            if s[j] not in my_set:
                my_set.add(s[j])
                maxlength= max(maxlength, j-i+1)
                
            else:
                while (s[j] in my_set):
                    my_set.remove(s[i])
                    i+=1
                my_set.add(s[j])
                    

        return maxlength
        