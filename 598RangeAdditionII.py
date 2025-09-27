class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        if not ops:
            return m*n
        min_x=ops[0][0]
        min_y=ops[0][1]
        for op in ops:
            min_x=min(min_x,op[0])
            min_y=min(min_y,op[1])
        return min_x*min_y
    
class TestApp:
      def testCaseOne(self):
          assert Solution().maxCount( m = 3, n = 3, ops =[[2,2],[3,3]])==4
      def testCaseTwo(self):
          assert Solution().maxCount( m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]])==4
      def testCaseThree(self):
          assert Solution().maxCount( m = 3, n = 3, ops = [])==9