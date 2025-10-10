class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_len=len(sentences[0].split(" "))
        n=len(sentences)
        for i in range(1,n):
            max_len=max(max_len,len(sentences[i].split(" ")))
        return max_len 

class TestApp:
    def testCaseOne(self):
        assert Solution().mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])==6 
    def testCaseTwo(self):
        assert Solution().mostWordsFound(["please wait", "continue to fight", "continue to win"])==3