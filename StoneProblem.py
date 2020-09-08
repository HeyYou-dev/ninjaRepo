# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
import heapq
from typing import List

class Solution:

    def lastStoneWeight(self, stones: List[int]):
        # first check lenth of collecton group of stone
        while len(stones) > 1:
            x = heapq.nlargest(2, stones)
            if x[0] == x[1]:
                stones.remove(x[0])
                stones.remove(x[1])
            else:
                stones.remove(x[0])
                stones.remove(x[1])
                stones.append(x[0]-x[1])
        else:
            if stones:
                return stones[0]
            else:
                return 0

# object instanciation
obj = Solution()
print(obj.lastStoneWeight([2, 7, 4, 1, 8, 1]))
