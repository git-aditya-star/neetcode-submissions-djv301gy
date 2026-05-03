class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        long = 0
        map = {}
        curr = 0
        start = 0
        for i in range(0, len(s)):
            char = s[i]
            if char not in map:
                curr +=1
            else:
                print(f"i - {i}")
                # print(start)
                new_start = map[char] + 1
                while start < new_start:
                    print(f"start {start} {s[start]}")
                    map.pop(s[start])
                    start+=1
                curr = i - start  + 1
            map[char] = i              
            long = max(long, curr)
        return long

        