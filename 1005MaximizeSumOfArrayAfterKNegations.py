'''

Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
 

Constraints:

1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104

'''

import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
              temp=heapq.heappop(nums)
              heapq.heappush(nums,-1*temp)
              k-=1
        return sum(nums)
        
class TestApp:
    def testCaseOne(self):
        assert Solution().largestSumAfterKNegations([4,2,3],1)==5
    def testCaseTwo(self):
        assert Solution().largestSumAfterKNegations([3,-1,0,2],3)==6
    def testCaseThree(self):
        assert Solution().largestSumAfterKNegations([2,-3,-1,5,-4],2)==13
    def testCaseFour(self):
        assert Solution().largestSumAfterKNegations([1,2,3],3)==4
    def testCaseFive(self):
        assert Solution().largestSumAfterKNegations([6,7,-4],1)==17