'''

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, 
switching the matrix's row and column indices.



 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109

'''

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows,cols=len(matrix),len(matrix[0])
        result=[[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(cols):
            for j in range(rows):
                result[i][j]=matrix[j][i]
        return result
class TestApp:
      def testCaseOne(self):
          assert Solution().transpose([[1,2,3],[4,5,6],[7,8,9]])==[[1,4,7],[2,5,8],[3,6,9]]
      def testCaseTwo(self):
          assert Solution().transpose([[1,2,3],[4,5,6]])==[[1,4],[2,5],[3,6]]
