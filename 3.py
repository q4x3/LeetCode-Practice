class Solution1:
    # 二分答案
    def checkNoRepeat(self, s: str) -> bool:
        # 判断s是否无重复字符
        alphabet = set()
        for tmp in s:
            if tmp in alphabet:
                return False
            else:
                alphabet.add(tmp)
        return True

    def checkLength(self, s: str, length: int) -> bool:
        # 判断s中是否存在长度为length的无重复字符子串
        sLen = len(s)
        for i in range(sLen + 1 - length):
            if self.checkNoRepeat(s[i: i + length]):
                return True
        return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        hi = len(s) + 1
        lo = 0
        while hi - lo > 1:
            mid = (hi + lo) // 2
            result = self.checkLength(s, mid)
            if result:
                lo = mid
                continue
            else:
                hi = mid
                continue
        return lo


class Solution2:
    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        sLen = len(s)
        result = 0
        alphabet = set()
        while end < sLen:
            tmp = s[end]
            while tmp in alphabet:
                removal = s[start]
                start += 1
                alphabet.remove(removal)
            alphabet.add(tmp)
            if result < end - start + 1:
                result = end - start + 1
            end += 1
        return result


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

solution = Solution2()
print(solution.lengthOfLongestSubstring(s1))
print(solution.lengthOfLongestSubstring(s2))
print(solution.lengthOfLongestSubstring(s3))
