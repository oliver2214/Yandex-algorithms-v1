from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        while l < r:
            m = (l + r) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1

        if l == len(letters):
            return letters[0]
        return letters[l]

s = Solution()
print(s.nextGreatestLetter(["x","x","y","y"], "z"))
