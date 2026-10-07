class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if not st or st[-1][0] != c:
                st.append([c, 1])
            elif st[-1][1] < k - 1:
                st[-1][1] += 1
            else:
                st.pop()
                
        res_list = []
        while st:
            p = st.pop()
            res_list.append(p[0] * p[1])
                
        return "".join(reversed(res_list))

        