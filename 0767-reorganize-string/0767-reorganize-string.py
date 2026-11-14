
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}

        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        max_heap = []

        for char in counts:
            heapq.heappush(max_heap, [-counts[char], char])

        res = ""
        prev_freq = 0
        prev_char = ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)

            res += char

            if prev_freq < 0:
                heapq.heappush(max_heap, [prev_freq, prev_char])

            freq += 1

            prev_freq = freq
            prev_char = char

        if len(res) == len(s):
            return res

        return ""
