from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        needed = tickets[k]
        if tickets[k] > 1:
            for i in range(len(tickets)):
                if needed > tickets[i]:
                    cur_needed = tickets[i]
                else:
                    cur_needed = needed - 1
                total += cur_needed
                tickets[i] = tickets[i] - cur_needed

        for i in range(k + 1):
            if tickets[i] > 0:
                total += 1
                tickets[i] = tickets[i] - 1

        return total


s = Solution()
print(s.timeRequiredToBuy([84,49,5,24,70,77,87,8], 3))
