class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for c in s:

            if len(stack)!=0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        result = ""

        while len(stack) != 0:
            t = stack[-1]      # TOP
            stack.pop()        # POP
            result += t

        return result[::-1]