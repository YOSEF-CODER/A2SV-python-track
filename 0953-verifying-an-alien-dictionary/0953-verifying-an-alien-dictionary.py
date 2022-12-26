class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet={char:index for index,char in enumerate(order)}
        
        words2=[]
        
        for w in words:
            temp=[]
            for ch in w:
                temp.append(alphabet[ch])
            words2.append(temp)
        for i in range(1,len(words2)):
            if words2[i-1] > words2[i]:
                return False
        return True
        
        