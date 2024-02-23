from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        t = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            t.append(h * 60 + m)

        t.sort()
        m = 1440
        t.append(t[-1] - 1440)
        for i in range(1, len(t)):
            m = min(m, t[i] - t[i - 1])
        return t

s = Solution()
s.findMinDifference
