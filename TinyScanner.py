ff = open("your path here")
s = ff.readline()
KeyWords = ["if", "then", "else", "end", "repeat", "until", "read", "write"]
Symbols = ['+', '-', '*', '/', '<', '>', '=', ':=', '(', ')', ';']
while len(s) != 0:		#Optimize this
    s = s.strip('\n').strip('\t').strip(' ')
    ind, temp2 = 0, 0
    while ind in range(len(s)):
        if s[ind] == ' ' or ind == len(s)-1 or s[ind] == '{':
            if len(s[temp2:ind]) > 0 or temp2 == len(s) - 1:
                if s[temp2:ind] in KeyWords or s[temp2:] in KeyWords:
                    if ind == len(s)-1:
                        if s[ind] != ';':
                            print s[temp2:], ": Reserved Word"
                        else:
                            print s[temp2:ind], ": Reserved Word"
                            print s[ind], ": Symbol"
                    else:
                        print s[temp2:ind], ": Reserved Word"
                    temp2 = ind + 1
                elif s[temp2:ind] in Symbols or s[temp2:] in Symbols:
                    if ind == len(s)-1:
                        print s[temp2:], ": Symbol"
                    else:
                        print s[temp2:ind], ": Symbol"
                    temp2 = ind + 1
                elif '0' <= s[temp2] <= '9':
                    Flag = False
                    for i in s[temp2:ind]:
                        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
                            Flag = True
                    if ind == len(s)-1:
                        if s[ind] != ';':
                            if Flag:
                                print s[temp2:], ": Digit error"
                            else:
                                print s[temp2:], ": Digit"
                        else:
                            if Flag:
                                print s[temp2:ind], ": Digit error"
                            else:
                                print s[temp2:ind], ": Digit"
                            print s[ind], ": Symbol"
                    else:
                        print s[temp2:ind], ": Digit"
                    temp2 = ind + 1
                elif 'a' <= s[temp2] <= 'z' or 'A' <= i <= 'Z':
                    Flag = False
                    for i in s[temp2:ind]:
                        if '0' <= i <= '9':
                            Flag = True
                    if ind == len(s)-1:
                        if s[ind] != ';':
                            if Flag:
                                print s[temp2:], ": Identifier error"
                            else:
                                print s[temp2:], ": Identifier"
                        else:
                            if Flag:
                                print s[temp2:ind], ": Identifier error"
                            else:
                                print s[temp2:ind], ": Identifier"
                            print s[ind], ": Symbol"
                    else:
                        print s[temp2:ind], ": Identifier"
                    temp2 = ind + 1
                else:
                    print s[temp2:ind], ": Unknown Symbol"
                    temp2 = ind + 1
            else:
                temp2 = ind + 1
            if s[ind] == '{':
                temp2 = ind
                ind = s[ind:].find('}') + ind
                print s[temp2:ind + 1], ": Comment"
                temp2 = ind + 1
        ind += 1
    print ""
    s = ff.readline()
ff.close()
