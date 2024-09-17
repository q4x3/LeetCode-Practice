class Solution1:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # 先暴力吧...
        result = set()
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)
        return list(result)

class Solution2:
    # 异或
    def min1(self, num):
        result = 1
        while num % 2 == 0:
            num //= 2
            result *= 2
        return result
    def listxor(self, nums: list[int]):
        result = 0
        for num in nums:
            result = num ^ result
        return result
    def singleNumber(self, nums: list[int]) -> list[int]:
        resultxor = self.listxor(nums)
        diffbit = self.min1(resultxor)
        result = [0, 0]
        for num in nums:
            if (num ^ diffbit) & diffbit:
                result[0] ^= num
            else:
                result[1] ^= num
        return result

nums = [1,2,1,3,2,5]
s = Solution2()
print(s.singleNumber(nums))
