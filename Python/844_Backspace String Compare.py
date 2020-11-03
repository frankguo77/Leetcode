class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def Getstr(s):
            s = list(s)
            i = 0
            for c in s:
                if c != "#":
                    s[i] = c
                    i += 1
                else:
                    if i:
                        i -= 1
            return s[:i]
        
        return Getstr(S) == Getstr(T)