
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


# 当一个问题的最优解包含其子问题的最优解时，称此问题具有最优子结构性质
# 问题的最优子结构性质是该问题可用贪心算法或动态规划算法求解的关键特征
#
# 贪心算法的基本思路是从问题的某一个初始解出发一步一步地进行，根据某个优化测度，每一步都要确保能获得局部最优解
# 每一步只考虑一个数据，他的选取应该满足局部优化的条件
# 若下一个数据和部分最优解连在一起不再是可行解时，就不把该数据添加到部分解中，直到把所有数据枚举完，或者不能再添加算法停止