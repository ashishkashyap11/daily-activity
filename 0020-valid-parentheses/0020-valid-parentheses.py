class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)
    
        for i in range(n):

            if s[i]=='[' or s[i]=='(' or s[i]=='{' :
                stack.append(s[i])

            elif len(stack)==0 and s[i] in ']})' :
                return False
            
            elif stack and stack[-1]=='[' and s[i]==']':
                stack.pop()

            elif stack and stack[-1]=='(' and s[i]==')':
                stack.pop()

            elif stack and stack[-1]=='{' and s[i]=='}':
                stack.pop()
                
            elif s[i] in ']})':
                return False
            
        if len(stack)!=0:
            return False

        return True

            
