'''
41. First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums. 
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 
Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''

def firstMissingPositive(nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        z = 0
        ra = len(nums)
        arr = [0]*(ra)
        for numb in nums:
            if numb > 0 and numb < (ra+1):
                arr[numb-1] = 1
        for z in range(ra):
             if arr[z] == 0:
                return z + 1
        return ra + 1


nums = [1,2,0]

print(firstMissingPositive(nums))