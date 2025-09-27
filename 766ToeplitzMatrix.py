'''

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99

'''
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m,n=len(matrix),len(matrix[0])
        
        for row in range(m):
            for col in range(n):
               value=matrix[row][col]
               if not self.topLeftSearch(row,col,m,n,matrix,value):
                   return False             
        return True
        
    def topLeftSearch(self,row:int,col:int,m:int,n:int,mat:list[list[int]],value:int):
        if row==m or col==n: return True 
        if mat[row][col]!=value:
            return False 
        return self.topLeftSearch(row+1,col+1,m,n,mat,value)

class TestApp:
      def testCaseOne(self):
          assert Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])==True 
      def testCaseTwo(self):
          assert Solution().isToeplitzMatrix([[1,2],[2,2]])==False 
      def testCaseThree(self):
          assert Solution().isToeplitzMatrix([[22,0,94,45,46,96],[10,22,80,94,45,46]])==False
      def testCaseFour(self):
          assert Solution().isToeplitzMatrix([[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]])==False