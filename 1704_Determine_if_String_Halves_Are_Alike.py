class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v="aeiouAEIOU"
        n=len(s)//2
        return sum(c in v for c in s[:n])==sum(c in v for c in s[n:])
        
