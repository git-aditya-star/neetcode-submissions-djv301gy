class Solution:
    



    
    
    def characterReplacement(self, s: str, k: int) -> int:

        def recalc(mp):
            h = [None ,-1]
            for key, value in mp.items():
                if value > h[1]:
                    h[0] = key
                    h[1] = value
            return h

        if len(s) <= k:
            return len(s)
        mp = {}
        highest = [-1, -1]
        long = k+1
        for i in range(k):
            ch = s[i]
            if ch not in mp:
                mp[ch] = 1
                if highest[1] == -1:
                    highest[0] = ch
                    highest[1] = 1
            else:
                count = mp[ch] +1
                if count > highest[1]:
                    highest[0] = ch
                    highest[1] = count
                
                mp[ch]+=1
        
        l = 0
        for r in range(k, len(s)):
            ch = s[r]
            if ch not in mp:
                mp[ch] = 1
            else:
                count = mp[ch] +1
                if count > highest[1]:
                    highest[0] = ch
                    highest[1] = count
                mp[ch]+=1
            count_not_highest = r - l +1 - highest[1]
            if count_not_highest > k:
                while count_not_highest > k and l < r :
                    l_val = s[l]
                    mp[l_val] -= 1
                    if mp[l_val] == 0:
                        mp.pop(l_val)

                    highest = recalc(mp)
                    l+=1
                    count_not_highest = r -l +1 - highest[1]
                    
            long = max(long , r -l +1)
        
        return long
            

        