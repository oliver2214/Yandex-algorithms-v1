class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l < r:
            m = (l + r) // 2
            sq = m * m
            if sq == num:
                return True
            if m * m >= num:
                r = m
            else:
                l = m + 1

        if l * l == num:
            return True
        return False


s = Solution()
print(s.isPerfectSquare(1))
