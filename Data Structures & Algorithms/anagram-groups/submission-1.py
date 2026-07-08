class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        output=[]

        for word in strs:
            sorted_word= "".join(sorted(word))

            if sorted_word not in anagram:
                anagram[sorted_word]=[]
            anagram[sorted_word].append(word)

        for value in anagram.values():
            output.append(value)
        
        return output




        