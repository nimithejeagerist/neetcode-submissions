class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        def idx(ch: str) -> int:
            return ord(ch) - ord('a')

        for i in s:
            index = idx(i)
            count[index] += 1
        
        for i in t:
            index = idx(i)
            count[index] -= 1
        
        return all(c == 0 for c in count)