class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr=[0] * len(words)
        answer=0

        for index,word in enumerate(words):
            for letter in word:
                arr[index] |= (1<<(ord(letter) - ord('a')))

        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] & arr[j] == 0:
                    answer=max(answer,len(words[i]) * len(words[j]))

        return answer