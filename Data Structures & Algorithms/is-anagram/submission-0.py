class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_1 = {}
        dict_2 = {}
        i=0
        for i in range(len(s)):
            dict_1[s[i]] = 1 + dict_1.get(s[i],0)
            dict_2[t[i]] = 1 + dict_2.get(t[i],0)

        return dict_1 == dict_2
                