class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = ''.join(ch for ch in s if ch.isalnum()).lower()
        return raw[::-1] == raw
        # if s==' ':
        #     return True
        # def helper(left,right):
        #     if left>right:
        #         return
        #     if s[left]!=s[right]:
        #         return False
        #     if left==right:
        #         return True
        #     return helper(left+1,right-1)

        # if helper(0,len(s)-1):
        #     return True
        # return False