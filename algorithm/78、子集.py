
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                res.append(x)
        return res


s = Solution()
nums = [1, 2, 3]

res = s.subsets(nums)

print(res)
print(res[:])