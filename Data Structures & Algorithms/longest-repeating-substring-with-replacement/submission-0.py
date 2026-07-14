class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap={}
        output=0

        i=0
        for j in range(len(s)):
            hashmap[s[j]] = 1 + hashmap.get(s[j],0)

            while (j-i+1)-max(hashmap.values()) > k:
                hashmap[s[i]]-=1
                i+=1
            output= max(output,j-i+1)
        return output
