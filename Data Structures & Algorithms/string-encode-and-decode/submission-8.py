class Solution:


    def encode(self, strs: List[str]) -> str:
        # encode a list of strings to a string
        # keep track lengths of each str, parse

        # runtime O(m): 
        # m is the sum of lengths of all the strings

        result = ""
        for i in range(len(strs)):
            length = len(strs[i])
            result += str(length) + "|"
            result += strs[i]
            
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        # decoded back to the original list of strings

        # runtime O(n)
        # m is the sum of lengths of all the strings
        # n is the number of strings
        parsed = list()
       
        st = s
         
        delimiter_index = st.find("|")
        while delimiter_index != -1:
            delimiter_index = st.find("|")
            curr_num = st[: delimiter_index]
            st = st[delimiter_index + 1 :]

            if (len(st) == int(curr_num)):
                parsed.append(st)
                break;
            else:
                parsed.append(st[: int(curr_num)])
                st = st[int(curr_num) : ]

    
        return parsed



