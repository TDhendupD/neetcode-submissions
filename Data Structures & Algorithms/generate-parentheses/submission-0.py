class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(word: str, left: int, right: int):
            if (left == n and right == left):
                ans.append(word)
                return
            if (left<n):
                helper(word + "(", left+1, right)
            if (right<left):
                helper(word + ")", left, right+1)
        helper("", 0, 0)
        return ans
            