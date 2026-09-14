class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        tmb = [0] * 256
        for char in t:
            tmb[ord(char)] += 1

        required = 0
        for i in range(256):
            if tmb[i] > 0:
                required += 1

        smb = [0] * 256
        low = 0
        matched = 0

        min_len = float('inf')
        min_start = -1

        for high in range(len(s)):
            right_char = s[high]
            smb[ord(right_char)] += 1

            if tmb[ord(right_char)] > 0 and smb[ord(right_char)] == tmb[ord(right_char)]:
                matched += 1

            while matched == required:

                current_len = high - low + 1
                if current_len < min_len:
                    min_len = current_len
                    min_start = low

                left_char = s[low]
                smb[ord(left_char)] -= 1

                if tmb[ord(left_char)] > 0 and smb[ord(left_char)] < tmb[ord(left_char)]:
                    matched -= 1

                low += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_start : min_start + min_len]