import collections

class Solution:
    def countCharacters(self, words, chars: str) -> int:
        ans = 0
        char_count = collections.Counter(chars)
        for word in words:
            wordc_count = collections.Counter(word)
            for c in wordc_count:
                if wordc_count[c] > char_count[c]:
                    break
            else:
                ans += len(word)
        return ans