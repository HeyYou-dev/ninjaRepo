# problem:2
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]

# Complexcity time: O(n)+O(1)[worst case n insertion in hash table], Space Complexcity O(n)
class Solution:
    def twoSum(self, nums, target):
        temp=[]
        dic =dict()
        for i in range(0, len(nums)):
            if(target-nums[i]) in dic:
                result =list((nums.index(target-nums[i]), nums.index(nums[i])))
                temp.append(result)
            dic[nums[i]]=nums[i]
        return temp
nums = [3,2,1,0]
target = 3
solution = Solution()
print(solution.twoSum(nums,target))
