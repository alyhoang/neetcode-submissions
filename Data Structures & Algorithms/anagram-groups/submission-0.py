class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # runtime: O(m * n)
        # m = num of strings 
        # n = length of the longest string
        map = dict()

        for word in strs:
            # sort each string by alphabet
            s = "".join(sorted(word))

            # put into map structure
                # key = sorted
                # value = list of strings
            if s in map:
                map[s].append(word)
            else:
                map[s] = [word]
        
        output = list()
        for key, value in map.items():
            output.append(value)

        return output

            

            
            

            