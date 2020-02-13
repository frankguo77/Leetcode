class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        if n == 0:
            return True
        idx = 0
        while idx < n:
            if data[idx] & 0x80 == 0:
                idx += 1
                continue
                
            if data[idx] & 0b11100000 == 0b11000000:
                if idx + 1 >= n or data[idx + 1] & 0b11000000 != 0b10000000:
                    return False
                idx += 2
                continue

            if data[idx] & 0b11110000 == 0b11100000:
                for i in range(1,3):
                    if idx + i >= n or data[idx + i] & 0b11000000 != 0b10000000:
                        return False
                idx += 3
                continue 
                
            if data[idx] & 0b11111000 == 0b11110000:
                for i in range(1,4):
                    if idx + i >= n or data[idx + i] & 0b11000000 != 0b10000000:
                        return False
                idx += 4
                continue
                
            return False
        
        return True
 