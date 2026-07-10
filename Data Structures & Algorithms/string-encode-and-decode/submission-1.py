class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstrs = ""
        for s in strs:
            encodedstrs += str(len(s)) + "#" + s
        return encodedstrs

    def decode(self, s: str) -> List[str]:

        decodedstrs = []
        i=0

        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            decodedstrs.append(s[j+1:j+1+length])
            i= j+1+length
        return decodedstrs

