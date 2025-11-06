'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

'''

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        sum_value=float('inf')
        nums.sort()
        n,result=len(nums),0
        for i in range(2,n):
            temp=nums[i-2]+nums[i-1]+nums[i]
            diff=abs(temp-target)
            if diff<sum_value:
                sum_value=diff 
                result=temp 
        return result 
class TestApp:
    def testCaseOne(self):
        assert Solution().threeSumClosest([-1,2,1,-4],1)==2 
    def testCaseTwo(self):
        assert Solution().threeSumClosest([0,0,0],1)==0 