class Solution:
    def repeatedNTimes(self, nums:list[int]) -> int:
        hash_map={}
        for num in nums:
            if num in hash_map: return num 
            hash_map[num]=1

class TestApp:
      def testCaseOne(self):
          assert Solution().repeatedNTimes([1,2,3,3])==3
      def testCaseTwo(self):
          assert Solution().repeatedNTimes([2,1,2,5,3,2])==2
      def testCaseThree(self):
          assert Solution().repeatedNTimes([5,1,5,2,5,3,5,4])==5
