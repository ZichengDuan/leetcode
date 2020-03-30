import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dicts = collections.Counter(s)
        num = 0
        flag = -1
        for i in dicts:
            if dicts[i] % 2 == 0:
                num += dicts[i]
            else:
                if dicts[i] == 1 and flag == -1:
                    num += 1
                    flag = 1
                if dicts[i] > 1:
                    num += dicts[i] - 1
                    if flag == -1:
                        num += 1
                        flag = 1
        return num