import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = []

        for i in range(len(capital)):
            pair = [capital[i], profits[i]]
            projects.append(pair)

        projects.sort()

        maxheap = []
        idx = 0
        n = len(projects)

        for i in range(k):

            while idx < n and projects[idx][0] <= w:
                heapq.heappush(maxheap, -projects[idx][1])
                idx += 1

            if not maxheap:
                break

            topp = -heapq.heappop(maxheap)
            w += topp

        return w