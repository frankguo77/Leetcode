class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_a = collections.Counter(ransomNote)
        count_b = collections.Counter(magazine)
        
        if len(count_b) < len(count_a): return False
        
        for ch, cn in count_a.items():
            if ch not in count_b: return False
            if count_b[ch] < cn: return False
        
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        return not any(ransomNote.count(i) > magazine.count(i) for i in set(ransomNote))