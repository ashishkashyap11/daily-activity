class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        need = [0] * 256
        for char in t:
            need[ord(char)] += 1

        required = 0
        for i in range(256):
            if need[i] > 0:
                required += 1

        have = [0] * 256
        matched = 0   

        low = 0
        res = float('inf')
        start = -1

        for high in range(len(s)):
            right_char = ord(s[high])
            have[right_char] += 1

            if need[right_char] > 0 and have[right_char] == need[right_char]:
                matched += 1

            while matched == required:
                length = high - low + 1
                if res > length:
                    res = length
                    start = low

                left_char = ord(s[low])
                have[left_char] -= 1

                if need[left_char] > 0 and have[left_char] < need[left_char]:
                    matched -= 1

                low += 1

        if res == float('inf'):
            return ""

        return s[start:start + res]