class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        word1.reverse()
        word2.reverse()
        print(word1)
        word=[]
        if len(word1) >= len(word2):
            n=len(word2)
        else:
            n=len(word1)

        for i in range(n):
            word.append(word1.pop())
            word.append(word2.pop())
            
        if word1 != []:
            for x in range(len(word1)):
                word.append(word1.pop())
        elif word2 != []:
            for x in range(len(word2)):
                word.append(word2.pop())
                
        s=''.join(word)
        return s