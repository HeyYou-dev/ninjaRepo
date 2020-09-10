

# problem:2
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
class Solution:
    def twoSum(self, nums, target):
        temp = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    result = list([i, j])
                    temp.append(result)
        return temp
nums = [3, 5, 2, -4, 8, 11]
target = 7
solution = Solution()
print(solution.twoSum(nums,target))
