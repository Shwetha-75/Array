class Solution:
    def uniquePaths(self, m: int, n: int,row:int=0,col:int=0) -> int:
        if row==m-1 or col==n-1: return 1 
        return self.uniquePaths(m,n,row+1,col)+self.uniquePaths(m,n,row,col+1)
class TestApp:
    def testCaseOne(self):
        assert Solution().uniquePaths(3,7)==28 
    def testCaseTwo(self):
        assert Solution().uniquePaths(3,2)==3    