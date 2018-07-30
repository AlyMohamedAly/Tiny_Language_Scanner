def NumOrVar(A):
    if 'a' <= A[0] <= 'z' or 'A' <= A[0] <= 'Z':
        return ProperVariable(A)
    elif '0' <= A[0] <= '9':
        return ProperInt(A)
    else:
        return "NaN"


def ProperVariable(A):
    for k in A:
        if not ('a' <= k <= 'z' or 'A' <= k <= 'Z' or '0' <= k <= '9'):
            return "NaN"
    return "Variable"


def ProperInt(A):
    for k in A:
        if not ('0' <= k <= '9'):
            return "NaN"
    return "Number"


def SplitSymb(A):
    temp = A
    for k in Symbols:
        if k in A:
            temp = (" " + k + " ").join(temp.split(k))
    return temp

KeyWords = ["if", "then", "else", "end", "repeat", "until", "read", "write"]
Symbols = ['+', '-', '*', '/', '<', '>', ':=', '(', ')', ';', '{', '}']
print ""
ff = open("F:\Input.txt", 'r')
text = ff.readlines()
ff.close()

for s in text:
    s = ((s.strip('\n')).strip('\t')).strip(' ')
    s = (SplitSymb(s).strip(' ')).split()
    i, sz = 0, len(s)
    while i < sz:
        if s[i] in KeyWords:
            print s[i] + " : KeyWord"
        elif s[i] in Symbols:
            if s[i] == '{':
                temp = s.index('}')
                print ' '.join(s[i+1:temp]) + " : Comment"
                i = temp+1
            else:
                print s[i] + " : Symbol"
        else:
            x = NumOrVar(s[i])
            if x == "Nan":
                print s[i] + " : Syntax Error"
            elif x == "Variable":
                print s[i] + " : Variable"
            elif x == "Number":
                print s[i] + " : Number"
        i += 1
    print ""
