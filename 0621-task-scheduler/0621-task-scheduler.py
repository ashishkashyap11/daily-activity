class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        fq = {}

        for i in range(len(tasks)):
            if tasks[i] in fq:
                fq[tasks[i]] += 1
            else:
                fq[tasks[i]] = 1

        ans = max(fq.values())

        count = 0

        for i in fq:
            if fq[i] == ans:
                count += 1

        no = (ans - 1) * (n + 1) + count

        return max(len(tasks), no)