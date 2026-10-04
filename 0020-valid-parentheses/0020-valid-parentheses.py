class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
    
        for i in range(n):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])

            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            elif s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            
        if len(stack) == 0:
            return True
        else:
            return False

