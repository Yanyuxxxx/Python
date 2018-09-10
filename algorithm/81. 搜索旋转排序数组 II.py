# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
# 示例 2:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false

class Solution:

    def search(self, nums, target):

        l, r = 0, len(nums) - 1

        if not nums:
            return False
        right = len(nums) - 1
        left = 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            if nums[left] < nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[left] > nums[middle]:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                left += 1

        return False


s = Solution()
nums = [2, 5, 6, 7, 0, 1, 2]
target = 2
print(s.search(nums, target))