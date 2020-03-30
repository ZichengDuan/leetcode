class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        n = len(nums)
        for i in range(n):
            # 记下值和index
            hash[nums[i]] = i
        for i in range(n):
            j = hash.get(target - nums[i])
            if j is not None and j != i:
                return [i, j]