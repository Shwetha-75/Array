'''

Given a non-empty array of non-negative integers nums, the degree of this array is
defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''
class Solution:
      def degreeOfArray(self,nums:list[list[int]]):
          hash_map={}
          for i in range(len(nums)):
              if nums[i] not in hash_map:
                  hash_map[nums[i]]=[1,[i]]
              else:
                  hash_map[nums[i]][0]+=1
                  hash_map[nums[i]][1].append(i)
          smallest_size=-1
          larger_frequency=0 
          for key in hash_map:
              value=hash_map[key]
              if value[0]==larger_frequency:
                  smallest_size=min(smallest_size,value[1][-1]-value[1][0]+1)
              if value[0]>larger_frequency:
                  larger_frequency=value[0]
                  smallest_size=value[1][-1]-value[1][0]+1
          return smallest_size 
class TestApp:
      def testCaseOne(self):
          assert Solution().degreeOfArray([1,2,2,3,1])==2
      def testCaseTwo(self):
          assert Solution().degreeOfArray([1,2,2,3,1,4,2])==6
    