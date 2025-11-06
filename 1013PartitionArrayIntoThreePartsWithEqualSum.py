'''
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104

'''

class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        left_sum=right_sum=0 
        n=len(arr)
        left,right=0,n-1 
        total=sum(arr)
        while left<right-1:
            left_sum+=arr[left]
            while right-1>left and right_sum!=left_sum:
                  right_sum+=arr[right]
                  right-=1
            if left_sum==right_sum and (total-(left_sum+right_sum)==right_sum):
                return True 
            left+=1
        left,right=0,n-1 
        left_sum=right_sum=0 
        
        while left<right-1:
            left_sum+=arr[left]
            while left<right-1 and right_sum!=left_sum:
                  left_sum+=arr[left]
                  left+=1
            if left_sum==right_sum and (total-(left_sum+right_sum)==right_sum):
                return True 
            right-=1
            
        left,right=0,n-1 
        left_sum=right_sum=0 
        
        while left<right-1:
            left_sum+=arr[left]
            right_sum+=arr[right]
            if left_sum==right_sum and (total-(left_sum+right_sum)==right_sum):
                return True 
            left+=1
            right-=1
        
        return False 
class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        parts=0
        total=sum(arr)
        if total%3: return False 
        sum_value=0
        for i in range(len(arr)):
            sum_value+=arr[i]
            if sum_value==((parts+1)*total//3):
                parts+=1
        return parts>=3
class TestApp:
    def testCaseOne(self):
        assert Solution().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])==True 
    def testCaseTwo(self):
        assert Solution().canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])==False 
    def testCaseThree(self):
        assert Solution().canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])==True  
        
