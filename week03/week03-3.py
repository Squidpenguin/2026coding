#week03-3.py
#1456
#母音aeiou 長度k的字串 最多幾個母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') #把母音變成一個set 用for c in vowels 就可以快速確認
        count = 0
        for i in range(k):
            if s[i] in vowels: count += 1
        ans = count
        N = len(s)
        for i in range(k, N):
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -=1
            ans = max(ans,count)
        return ans
