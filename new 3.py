 def IsComment(indx):
     while indx > -1:
         if s[indx] == '}':
             return False
         if s[indx] == '{':
             return True
         indx -= 1
     return False


 s = "testtttta > sssdsd then 250 mara {comment until 232323 < kmaaaan ya 33434aaam} x := 002 end;"
KeyWords = ["if", "then", "else", "end", "repeat", "until", "read", "write"]
Symbols = ['+', '-', '*', '/', '<', '>', '=', ':=', '(', ')']
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CapLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K' 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SMLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print " "
 for i in KeyWords:
     if i in s:
         if not IsComment(s.find(i)):
             print i, ": Reserved Word"

			 
 for j in Symbols:
     if j in s:
         if not IsComment(s.find(j)):
             print j, ": Special Symbol"


 Comment = s.find("{")
 if Comment != -1:
     Comment2 = s.find("}")
     print s[Comment:Comment2+1], ": Comment"

  Words = []
  Symbol = []
  for i in KeyWords:
      Words.append(s.find(i))
 
  for i in Symbols:
      Symbol.append(s.find(i))

 ind = 0
 while ind in range(len(s)):
     if s[ind] == '{':
         ind = s[ind:].find('}')
     if s[ind] in Digits:
         temp2 = ind
         while s[temp2] in Digits:
             if temp2 < len(s)-1:
                 temp2 += 1
         print s[ind:temp2], ": Digit"
         ind = temp2
     ind += 1
 ind = 0
 temp2 = 0
 while ind in range(len(s)):
     if s[ind] == ' ':
         if s[temp2:ind+1] not in KeyWords and s[temp2:ind+1] not in Symbols:
             print s[temp2:ind+1], ": ID"
             temp2 = ind + 1
      if s[ind] == '{':
           if len(s[temp2:ind]) > 0 and s[temp2:ind] not in KeyWords and s[temp2:ind] not in Symbols:
               print s[temp2:ind], ": ID"
           else:
          ind = s[ind:].find('}')
          temp2 = ind + 1
     ind += 1
