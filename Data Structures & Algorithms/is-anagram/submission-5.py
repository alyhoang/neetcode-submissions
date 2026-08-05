class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        one array approach:
        26 static array
        '''
        ASCII_VALUE = 96
        letters = [0] * 26
        score = 0

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_index = ord(s[i]) - ASCII_VALUE
            t_index = ord(t[i]) - ASCII_VALUE

            letters[s_index - 1] += 1
            letters[t_index - 1] -= 1
            #print("s: " + str(s_letter))
            #print("t: " + str(t_letter))
            #print("score: " + str(score))

        for i in range(len(letters)):
            print(letters[i])
            if letters[i] != 0:
                return False
        
        return True;

        

        