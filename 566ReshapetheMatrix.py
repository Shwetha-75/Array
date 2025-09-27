'''

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix 
into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the
number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original 
matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, 
output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300

'''

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        row,col=len(mat),len(mat[0])
        if row*col!=r*c:
            return mat
        auxillary_stack=[]

        for i in range(row):
            for j in range(col):
                auxillary_stack.append(mat[i][j])
        result_mat=[[0 for _ in range(c)] for _ in range(r)]     

        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                result_mat[i][j]=auxillary_stack.pop()
        return result_mat
    
class TestApp:
      def testCaseOne(self):
          assert Solution().matrixReshape([[1,2],[3,4]],1,4)==[[1,2,3,4]]
      def testCaseTwo(self):
          assert Solution().matrixReshape([[1,2],[3,4]],2,4)==[[1,2],[3,4]]