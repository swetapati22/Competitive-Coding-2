# Time Complexity :
- O(n), where n is the length of the input list `nums`

# Space Complexity :
- O(n), for storing the hashmap of seen numbers and their indices

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for pt_idx, pt_val in enumerate(nums):
            complement = target - pt_val
            if complement in num_to_index:
                return [pt_idx, num_to_index[complement]]

            num_to_index[pt_val] = pt_idx
