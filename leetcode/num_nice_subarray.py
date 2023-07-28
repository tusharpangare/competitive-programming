#https://leetcode.com/problems/count-number-of-nice-subarrays/
'''
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
'''

class Solution:
    def countNiceSubarrays(nums, k):
        count = 0
        prefixSum = [0] * len(nums)
        freq = {0: 1}

        prefixSum[0] = 1 if nums[0] % 2 == 1 else 0
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] + (1 if nums[i] % 2 == 1 else 0)

        for i in range(len(prefixSum)):
            if prefixSum[i] - k in freq:
                count += freq[prefixSum[i] - k]
            freq[prefixSum[i]] = freq.get(prefixSum[i], 0) + 1

        return count
