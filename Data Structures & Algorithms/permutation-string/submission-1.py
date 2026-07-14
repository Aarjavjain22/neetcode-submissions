class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        dict_1 = [0]*26
        dict_2 = [0]*26
        
        for i in range(len1):
            dict_1[ord(s1[i])-ord('a')] +=1
            dict_2[ord(s2[i])-ord('a')] +=1
            
        if dict_1 == dict_2:
            return True
            
        for r in range(len1, len2):
            dict_2[ord(s2[r])-ord('a')] += 1
            dict_2[ord(s2[r-len1]) -ord('a')] -=1
            
            if dict_1== dict_2:
                return True
        return False
                
