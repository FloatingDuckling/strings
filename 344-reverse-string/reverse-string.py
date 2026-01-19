class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s_rev = s.reverse() #too easy

      #          rev_s = " "
       #         i = 0
       #         while i < len(s):
        #            rev_s = s[i] + rev_s
        #            i = i + 1        
         #       s = rev_s

        # 2 index approach, swap the left and right indexes of s

        l = 0 #starting index
        r = len(s) - 1 #last index

        while l < r: #if they are equal, it mean the characters are all swapped
            s[l], s[r] = s[r], s[l] #assign the respective values
            l = l + 1
            r = r - 1
        