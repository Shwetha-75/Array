class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        for i in range(n):
            nums[i]=1 if nums[i]%2 else 0 
        nums.sort()
        return nums 

class TestApp:
    def testCaseOne(self):
        assert Solution().transformArray([1,5,1,4,2])==[0,0,1,1,1]
    def testCaseTwo(self):
        assert Solution().transformArray([4,3,2,1])==[0,0,1,1]