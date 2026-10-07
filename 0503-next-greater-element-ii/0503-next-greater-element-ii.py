class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack=[]
        ans=[]
        n=len(nums)

        for j in range(n-2,-1,-1):
            stack.append(nums[j])

        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(nums[i])

        rev = ans[::-1]
        return rev
            

