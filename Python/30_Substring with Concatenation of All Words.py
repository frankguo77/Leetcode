class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0:
            return []
        
        word_count = len(words)
        if word_count == 0:
            return []
        
        word_len = len(words[0])
        
        counter = collections.Counter(words)
        res = []
        for i in range(len(s) - word_len * word_count + 1):
            if s[i:i + word_len] in counter:
                tempcounter = collections.Counter()
                for j in range(word_count):
                    ss = s[i + j*word_len : i + (j + 1) * word_len]
                    if ss in counter:
                        tempcounter[ss] += 1
                        if tempcounter[ss] > counter[ss]:
                            #print("here")                      
                            break
                    else:
                        #print("There")
                        break
                else:
                    #print("There")
                    res.append(i)       
                               
                    
                # tempcounter = collections.Counter([s[i + j*word_len : i + (j + 1) * word_len] for j in range(word_count)])
                # if tempcounter == counter:
                #     res.append(i)
        return res
                    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0:
            return []
        
        word_count = len(words)
        if word_count == 0:
            return []
        
        word_len = len(words[0])
        
        res = []
        for i in range(word_len):
            l = r = i
            counter = collections.Counter(words)
            notmatch = len(counter)
            # print(l, r, notmatch)
            while r < len(s) - word_len + 1:
                ss = s[r:r + word_len]
                # print(l,r,ss)
                if ss in counter:
                    counter[ss] -= 1
                    if counter[ss] == 0:
                        notmatch -= 1
                r += word_len
                
                if r - l > word_count * word_len:
                    ss = s[l:l + word_len]
                    if ss in counter:
                        counter[ss] += 1
                        if counter[ss] == 1:
                            notmatch += 1
                    
                    l += word_len
                            
                if notmatch == 0:
                    res.append(l)
                    
                   
                    
                # tempcounter = collections.Counter([s[i + j*word_len : i + (j + 1) * word_len] for j in range(word_count)])
                # if tempcounter == counter:
                #     res.append(i)
        return res        
                
            
            
        
        