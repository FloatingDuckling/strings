class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Linked the repo
        #first check if the length of "pattern" matches "s"
        #for that, split the words
        s = s.split()

        if len(pattern) != len(s):
            return False 

        #Now map char of "s" to words of "pattern"

        dict = {} #to store the char - word mapping
        s1 = set() #to store words to char mapping, it is an empy set now

        for i in range(len(pattern)):  #the same can be written with enumerate
            c = pattern[i] #i is index, c is char corresponding to that index
            if c not in dict:
                if s[i] in s1: #checks if first word is already mapped to a character and stores in s1
                    return False 
                dict[c] = s[i] #assign the same index work to same index position in dict
                s1.add(s[i]) #also store in the set
            else: #if it is already in dict, check if it maps to the right word
                if dict[c] != s[i]:
                    return False
        return True



                
