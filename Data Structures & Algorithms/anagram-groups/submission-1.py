class Solution:
    


    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        def create_map(string):
            map = {}
            for c in string:
                if c in map:
                    map[c]+=1
                else:
                    map[c]=0
            return map
        
        def compare_maps(map1, map2):
            if len(map1) != len(map2):
                return False
            
            for key, value in map1.items():
                if key not in map2:
                    return False
                if value != map2[key]:
                    return False
            return True

        list_of_maps = []
        result = []
        first = strings[0]
        list_of_maps.append(create_map(first))
        result.append([first])
        for idx in range(1, len(strings)):
            match = False
            current_map = create_map(strings[idx])
            current_len = len(current_map)
            for map_idx, map in enumerate(list_of_maps):
                if current_len == len(map) and compare_maps(current_map, map):
                    result[map_idx].append(strings[idx])
                    match = True
                    break
            if not match:
                result.append([strings[idx]])
                list_of_maps.append(current_map)
        return result
            
                

        