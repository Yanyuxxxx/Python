
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution:
    def maxSubArray(self, nums):
        sum = 0
        maxSum = nums[0]
        for index in range(len(nums)):
            sum += nums[index]
            if sum > maxSum:
                maxSum = sum
            if sum < 0:
                sum = 0
        return maxSum



nums = [-3,-2,0,-1]
s = Solution()
maxSum = s.maxSubArray(nums)
print(maxSum)