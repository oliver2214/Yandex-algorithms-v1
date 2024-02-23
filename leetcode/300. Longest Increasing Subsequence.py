from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m = 0
        rate = [0] * len(nums)
        for i in range(len(nums)):
            j = i - 1
            local_max = 0
            while j >= 0:
                if nums[j] < nums[i] and local_max < rate[j]:
                    local_max = rate[j]
                j -= 1
            rate[i] = local_max + 1
            m = max(m, rate[i])
        print(rate)
        return m


s = Solution()
print(s.lengthOfLIS([0,1,0,3,2,3]))
