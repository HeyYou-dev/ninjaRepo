# problem:2
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
# Complexcity time: O(n)+O(1)[worst case n insertion in hash table], Space Complexcity O(n)
import  math
class Solution:
                
    def twoSum(self, nums, target):
        p =0
        j = len(nums)-1
        for i in range(len(nums)):pass
        binarySearch(nums,p,len(nums)-1,3)
    # O(log) for one element

def binarySearch(nums,i,j,element):
    if (i == j):
        if (element == nums[i]):
            return i
    else:
        mid=math.ceil((i+j)/2)
        print(f'mid{mid}')
        if (element==nums[mid]):
            return mid
        elif (element<mid):
            binarySearch(nums,i,mid-1,element)
        else:
            print(f'mid{nums} {mid+1} {j} {element}')
            binarySearch(nums,mid+1,j,element)
nums = [0,1,2,3]
target = 3
solution = Solution()
print(solution.twoSum(nums,target))
