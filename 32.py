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
    def parentheses2zeros(self, s: str) -> str:
        stack = []
        for i, tmp in enumerate(s):
            if len(stack) and stack[-1][0] == "(" and tmp == ")":
                index = stack[-1][1]
                stack.pop()
                s = s[:index] + "0" + s[index+1:]
                s = s[:i] + "0" + s[i+1:]
            else:
                stack.append((tmp, i))
        return s
    def checkAns(self, ans: int, s: str) -> bool:
        lenS = len(s)
        for i in range(lenS - ans + 1):
            subS = s[i: i + ans]
            try:
                if int(subS) == 0:
                    return True
            except Exception as e:
                continue
        return False
    def longestValidParentheses(self, s: str) -> int:
        s = self.parentheses2zeros(s)
        lo = 0
        hi = len(s) + 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.checkAns(mid, s):
                lo = mid
            else:
                hi = mid
        return lo

class Solution3:
    def parentheses2zeros(self, s: str) -> list:
        stack = []
        s_list = list(s)
        for i, tmp in enumerate(s_list):
            if len(stack) and stack[-1][0] == "(" and tmp == ")":
                index = stack[-1][1]
                stack.pop()
                s_list[index] = 0
                s_list[i] = 0
            else:
                stack.append((tmp, i))
        return s_list
    def longestValidParentheses(self, s: str) -> int:
        s_list = self.parentheses2zeros(s)
        left = 0
        right = 0
        result = 0
        while right < len(s_list):
            if s_list[right] == 0:
                right += 1
                if result < right - left:
                    result = right - left
            else:
                right = left = right + 1
        return result
s = Solution3()
string = "())()()"
print(s.longestValidParentheses(string))