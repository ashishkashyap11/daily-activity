class Solution(object):

    def characterReplacement(self, s, k):

        low = 0
        freq = [0] * 256
        maxcnt = 0
        res = 0

        for high in range(len(s)):

            freq[ord(s[high])] += 1

            maxcnt = max(maxcnt, freq[ord(s[high])])

            length = high - low + 1

            diff = length - maxcnt

            while diff > k:

                freq[ord(s[low])] -= 1
                low += 1

                length = high - low + 1
                diff = length - maxcnt

            res = max(res, length)

        return res