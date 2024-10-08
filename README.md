# LeetCode-Practice 日记

欢迎来到我的 LeetCode 练习仓库！这是我在解决 LeetCode 问题过程中的记录和心得分享。希望这能帮助到自己，也许还能对其他有类似练习目标的开发者有所帮助。

## 📅 练习日志

### 2024.9.26

**今天的目标：** 写出32的通过解法

1. **问题**: [32. 最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/description/)
   - **思路**: 栈模拟判断括号有效性，有效则置0，之后计算最长连续0
   - **结果**: 过，但用时长

**心得体会：** 
   - python里str是不可变的，想要改某个index需要切片（或者转list再改）
   - 连续0用滑窗

### 2024.9.18

**今天的目标：** 一题，至少写出暴力解法

1. **问题**: [32. 最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/description/)
   - **思路**: 暴力
   - **结果**: 超时

**心得体会：** 
   - python里用list来模拟栈
   - 明天写另一个解法


### 2024.9.17

**今天的目标：** 一题，至少写出暴力解法

1. **问题**: [260. 只出现一次的数字 III](https://leetcode.cn/problems/single-number-iii/description/)
   - **思路**: 暴力
   - **结果**: 过，但不符合空间复杂度要求
   - **思路**: 异或运算，相同数异或为0（被gpt提示了异或的思路）
   - **结果**: 过

**心得体会：** 
   - 相同数异或运算结果为0
   - 如果要计算某个数二进制某一位的值，与运算


### 2024.9.16

**今天的目标：** 一题，至少写出暴力解法

1. **问题**: [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
   - **思路**: 二分答案（把原本的list换成set）
   - **结果**: 勉强过
   - **思路2**: 滑动窗口（被gpt提示了滑动窗口的思路）
   - **结果**: 过

**心得体会：** 
   - 字符串相关题目应当考虑空串
   - 滑动窗口是xxx最长子串的可行解
   - set的删除、查找都是O(1)
## 📚 资源与参考

- [LeetCode 题目列表](https://leetcode.com/problemset/all/)
- [算法与数据结构学习资源](https://github.com/TheAlgorithms/Python)

## 📝 计划与目标

- 每周解决 5 道 LeetCode 题目（CodeTop按最近考察时间排序），涵盖不同的算法和数据结构。
- 定期回顾并优化解决方案，以提高代码效率和清晰度。

Happy Coding! 🎉

