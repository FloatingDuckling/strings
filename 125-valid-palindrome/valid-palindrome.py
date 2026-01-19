class Solution:
    def isPalindrome(self, s: str) -> bool:
        #ch = {",", ":", ".", "/", "@", "#", "*", "!", "&", "_", "-", "(", ")", "{", "}", "[", "]", "\"", "'"}
         # ch is dictionary of symbols, can't keep writing it manually. Check for alphanumeric

        s_new = "" #declare a blank string
        for c in s:
            if c.isalnum():
                s_new = s_new + c #if string is alphanumeric, sotre in s_new
                s_new = s_new.lower() #change everything to lowercase .lower()
        s_new = "".join(s_new.split()) # remove blank spaces but s.split returns list, so use join to convert back to string


 #       for i in ch:
 #           s = s.replace(i, "") #remove the extra symbols
  #          s = s.lower()  #change everything to lowercase .lower()

   #     s = "".join(s.split()) 
#    print(s) #s is a list

        
        ## Now write a code to check if it's palindrome or not
        #option 1: check the first with last char, then move to second and second last, etc

        Palindrome = True
        for i in range(len(s_new)):
            if s_new[i] != s_new[len(s_new) - 1 - i]: #len(s) - 1 gives index of last character. len(s) - 1 - i gives index of last characte matching with i
                print("Not a palindrome")
                Palindrome = False
                return (Palindrome)
                break

        if Palindrome == True:
            print("Palindrome")
            return (Palindrome)
