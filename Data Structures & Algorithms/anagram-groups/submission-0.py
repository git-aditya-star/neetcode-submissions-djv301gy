class Solution:
    


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def set_in_ana(string: str) -> List[int]:
            anal = [0]* 26
            for c in string:
                idx = ord(c)-ord('a')
                anal[idx]+=1
            return anal

        def is_same_anal(anal: List[int], string:str)->bool:
            anal_dup = anal.copy()
            for c in string:
                idx = ord(c)-ord('a')
                anal_dup[idx]-=1
                if anal_dup[idx] < 0:
                    return False
            for i in range(26):
                if anal_dup[i] != 0:
                    return False
            return True
        

        result = []
        skipped_idx = set()
        for start in range(0, len(strs)):
            if start in skipped_idx:
                continue
            sublist = [strs[start]]
            ana_list = set_in_ana(strs[start])

            for itr in range(start+1, len(strs)):
                if itr in skipped_idx:
                    continue
                if is_same_anal(ana_list, strs[itr]):
                    skipped_idx.add(itr)
                    sublist.append(strs[itr])
            result.append(sublist)
        return result
                

        