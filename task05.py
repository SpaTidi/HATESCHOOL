"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
        maxSum = -99999999999999999

        for length in range(1, k + 1):
                curSum = sum(nums[:length])
                maxSum = max(curSum, maxSum)
            
                for i in range(length, len(nums)):
                        curSum += nums[i] - nums[i - length]
                        maxSum = max(curSum, maxSum)
        
        return maxSum

if __name__ == '__main__':
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        print(find_maximal_subarray_sum(nums, k))
        
        nums = [-1, -1, -2, -2, -2]
        k = 3
        print(find_maximal_subarray_sum(nums, k))
