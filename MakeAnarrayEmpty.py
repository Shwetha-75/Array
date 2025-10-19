class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        swap_count=0 
        temp_array=sorted(nums)
        for i in range(len(nums)):
            if  temp_array[i]!=nums[i]:
                swap_count+=1
        if swap_count:
            swap_count-=1
        return len(nums)+swap_count              
class TestApp:
    def testCaseOne(self):
        assert Solution().countOperationsToEmptyArray([3,4,-1])==5
    def testCaseTwo(self):
        assert Solution().countOperationsToEmptyArray([1,2,3])==3
    def testCaseThree(self):
        assert Solution().countOperationsToEmptyArray([1,2,4,3])==5
    def testCaseFour(self):
        assert Solution().countOperationsToEmptyArray([1,5,4,3])==5
        