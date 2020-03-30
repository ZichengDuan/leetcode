class Solution:
    def threeSum(self, nums):
        """
        :param nums:
        :return:
        """
        nums.sort()
        n = len(nums)
        res = []
        if n < 3:
            return []

        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1
        return res