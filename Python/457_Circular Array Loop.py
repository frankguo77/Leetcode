class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2: return False
        
        def nextpos(i):
            return (i + nums[i] % n + n) % n
        
        for i in range(n):
            f = s = i
            f = nextpos(i)
            while nums[i] * nums[f] > 0 and nums[i] * nums[nextpos(f)] > 0:
                s = nextpos(s)
                f = nextpos(nextpos(f))
                if f == s:
                    if s == nextpos(f):
                        break
                    return True

        return False

    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2: return False
        
        def nextpos(i):
            return (i + nums[i] % n + n) % n
        
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            f = s = i
            visited.add(f)
            while nums[i] * nums[f] > 0 and nums[i] * nums[nextpos(f)] > 0:
                s = nextpos(s)
                f = nextpos(nextpos(f))
                visited.add(f)
                if f == s:
                    if s == nextpos(f):
                        break
                    return True

        return False

    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = []
        m = collections.defaultdict(list)
        for vocab in d:
            m[vocab[0]].append((0,vocab))
            
        for c in s:
            wlist = m[c]
            del m[c]
            for idx, w in wlist:
                if idx + 1 == len(w):
                    ans.append(w)
                else:
                    m[w[idx + 1]].append((idx + 1, w))
                    
        if not ans: return ""
        maxl = len(max(ans, key = len))
        return min(w for w in ans if len(w) == maxl)
        
        