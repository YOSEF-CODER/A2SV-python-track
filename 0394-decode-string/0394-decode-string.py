class Solution:
    def decodeString(self, s: str) -> str:                         
        
        def recurse(s, pos):       
            result = ""
            i, num = pos, 0
            
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '[':
                    string, end = recurse(s, i + 1)
                    result += num * string
                    i = end
                    num = 0
                elif c == ']':
                    return result, i
                else:
                    result += c
                i += 1
            
            return result, i
                
        return recurse(s, 0)[0]