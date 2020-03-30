class Solution:
    def maxArea(self, height) -> int:
        i, j, MaxArea = 0, len(height) - 1, 0
        while i != j:
            area = (j - i) * min(height[i], height[j])
            if area > MaxArea:
                MaxArea = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return MaxArea