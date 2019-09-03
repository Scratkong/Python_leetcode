# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # save result
        res_list = []
        # sort nums
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                # if min > o its impossible that the sum of three nums is 0
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) -1
            while j < k:
                # check whether the sum of three nums is 0
                if nums[j] + nums[k] == -nums[i]:
                    res_list.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
            return res_list
