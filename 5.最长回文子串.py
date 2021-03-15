#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def expand(self, s, l, r):
        # expand as far as possible if the two letters are equal
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    def longestPalindrome(self, s: str) -> str:
        # start and end of the longest palindrome
        l, r = 0, 0
        for i in range(len(s)):
            # expand at each index
            l1, r1 = self.expand(s, i, i)
            l2, r2 = self.expand(s, i, i + 1)
            if r1 - l1 > r - l:
                l, r = l1, r1
            if r2 - l2 > r - l:
                l, r = l2, r2
        return s[l: r + 1]

'''
# HashMap method (self-written)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # {character: [appearances]}
        d = {}
        for (i, c) in enumerate(s):
            if c not in d:
                d[c] = []
            d[c].append(i)
        best = s[0];
        for (i, c) in enumerate(s):
            # search for palindromes at each index
            for j in range(len(d[c])-1, 0, -1):
                if d[c][j] == i: break;
                elif s[i:d[c][j]+1] == s[i:d[c][j]+1][::-1]:
                    best = s[i:d[c][j]+1] if d[c][j]-i+1 > len(best) else best
        return best
'''
# @lc code=end

