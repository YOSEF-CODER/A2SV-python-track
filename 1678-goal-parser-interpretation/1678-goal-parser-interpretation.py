class Solution:
    def interpret(self, command: str) -> str:
        i=0
        res=''
        while i < len(command):
            if command[i]=='G':
              res+='G'
            elif command[i] == '(' and command[i+1] == ')':
              res+='o'
              i+=1
            elif command[i] == '(' and command[i+1] == 'a':
              res+='al'
              if i+3 >= len(command):
               return res
            i+=1
        return res