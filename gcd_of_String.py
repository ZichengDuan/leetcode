class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                if str1 == ((len1 // i) * str1[:i]) and str2 == ((len2 // i) * str1[:i]):
                    return str1[:i]
        return ""