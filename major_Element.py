class Solution:
    def majorityElement(self, nums) -> int:
        hash = {}
        n = len(nums)
        if(n==1):
            return nums[0]
        max_count = n // 2
        for i in range(n):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1
                if hash[nums[i]] > max_count:
                    return nums[i]