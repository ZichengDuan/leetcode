class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        maxi = 0
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            longest += s[i]
            print(longest[:len(longest)-1], s[i], s[i] in longest[:len(longest)-1], len(longest[:len(longest) - 1]))
            if len(longest) != 1 and s[i] in longest[:len(longest)-1]:
                maxi = max(maxi, len(longest[:len(longest) - 1]))
                for j in range(len(longest[:len(longest) - 1])):
                    if longest[j] == s[i]:
                        break
                longest = longest[j + 1:]
            else:
                maxi = max(len(longest), maxi)
        return maxi