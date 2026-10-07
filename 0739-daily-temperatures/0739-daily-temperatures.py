class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        st=[]
        ans=[]
        st.append(n-1)
        ans.append(0)
        for i in range(n-2,-1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if not st:
                ans.append(0)
            else:
                top=st[-1]
                day=top-i
                ans.append(day)
            st.append(i)

        rev = ans[::-1]
        return rev

