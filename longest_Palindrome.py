class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        maxLength = 0
        maxStr = ""
        center = 0
        for i in range(len(s)):
            odd, tmpstr1 = self.centerExpand(s, i, i)
            even, tmpstr2 = self.centerExpand(s, i, i + 1)
            if maxLength < max(even, odd):
                center = i
                maxLength = max(even, odd)
                maxStr = tmpstr1 if len(tmpstr1) > len(tmpstr2) else tmpstr2

        return maxStr

    def centerExpand(self, s, begin, end):
        left = begin
        right = end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, s[left + 1: right]