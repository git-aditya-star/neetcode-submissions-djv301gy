class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        sizes = []
        for string in strs:
            sizes.append(str(len(string)))

        res = ",".join(sizes)
        res += "$"
        concatted_strs = "".join(strs)
        res += concatted_strs
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        sizes = []
        num = ""
        start_s = -1
        res = []
        print(s)
        for idx, ch in enumerate(s):
            if ch == "$":
                start_s = idx+1
                sizes.append(int(num))
                break 
            if ch != ',':
                num += ch
            else :
                sizes.append(int(num))
                num = ""
        for size in sizes:
            print(size)
            string = s[start_s: (start_s)+size]
            res.append(string)
            start_s = start_s+size
            
        return res
