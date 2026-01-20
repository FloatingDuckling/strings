class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        #indices = [] ## just incase i want to return both the index in haystack that start with "sad"

        for i in range (len(haystack)-len(needle)+1): #0 to 8 ## not clear why i range is this instead of len(haystack)
            for j in range(len(needle)):
                index = -1
                #print("print before j loop", "i=",i, "j=",j, haystack[i+j], needle[j])
                if needle [j] != haystack[i+j]:
                    #print("break with","i=",i, "j=",j)
                    #print("test index", index)
                    break # only if the condition is met, break the j loop

                if needle[j] == haystack[i+j]:
                    #print ("i =", i, "j =", j, end="\n")
                    index = i

            if index != -1:
                #indices.append(index)
                return(i)

        return(-1)