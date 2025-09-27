class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        n=len(nums)
        temp=[0]*len(divisors)
        for i in range(len(divisors)):
            count=0 
            for j in range(n):
                if not nums[j]%divisors[i]:
                    count+=1
            temp[i]=count 
        max_count=0
        value=divisors[0]
        for i in range(len(temp)):
            if temp[i]>max_count:
                max_count=temp[i] 
                value=divisors[i]
            elif max_count==temp[i]:
                value=min(value,divisors[i])
        return value
    
class TestApp:
      def testCaseOne(self):
          assert Solution().maxDivScore([2,9,15,50],[5,3,7,2])==2 
      def testCaseTwo(self):
          assert Solution().maxDivScore([4,7,9,3,9],[5,2,3])==3
      def testCaseThree(self):
          assert Solution().maxDivScore([20,14,21,10],[10,16,20])==10
