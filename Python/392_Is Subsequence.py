class Solution:
    # slolution 1: two pointer
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)

    # slolution 2: queque
    def isSubsequence2(self, s: str, t: str) -> bool:
        q = collections.deque(s)
        
        for c in t:
            if not q: return True
            if c == q[0]: q.popleft()
        return not q

     # slolution 3: stack
    def isSubsequence3(self, s: str, t: str) -> bool:
        s = list(s)
        
        for c in t[::-1]:
            if not s: return True
            if c == s[-1]: s.pop()
        return not s

     # slolution 4: greedy
    def isSubsequence4(self, s: str, t: str) -> bool:
        index = -1
        for char in s:
            try:
                index = t.index(char, index + 1)
            except:
                return False
        return True