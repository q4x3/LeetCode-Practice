class Solution1:
    # 暴力
    def isValidParentheses(self, s: str) -> bool:
        stack = []
        for tmp in s:
            if len(stack) and stack[-1] == '(' and tmp == ')':
                stack.pop()
            else:
                stack.append(tmp)
        if len(stack):
            return False
        else:
            return True
    def checkAns(self, ans: int, s: str) -> bool:
        lenS = len(s)
        for i in range(lenS - ans + 1):
            subS = s[i: i + ans]
            if self.isValidParentheses(subS):
                return True
        return False
    def longestValidParentheses(self, s: str) -> int:
        for i in range(len(s), -1, -1):
            if self.checkAns(i, s):
                return i


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        pass

s = Solution2()
string = ""
print(s.longestValidParentheses(string))