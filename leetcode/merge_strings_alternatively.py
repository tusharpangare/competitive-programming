class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out=""
        i=len(word1)+len(word2)
        while i>0:
            if len(word1)>0:
                out+=word1[0]
                word1=word1[1:]
                i-=1
            if len(word2)>0:
                out+=word2[0]
                word2=word2[1:]
                i-=1        
        return out
    
obj= Solution()
res=obj.mergeAlternately("cf","eee") 
print(res)   

              