 s = "testtttta > sssdsd then 250 mara {comment until 232323 < kmaaaan ya 33434aaam} x := 002 end;"
KeyWords = ["if", "then", "else", "end", "repeat", "until", "read", "write"]
Symbols = ['+', '-', '*', '/', '<', '>', '=', ':=', '(', ')']

ind, temp2 =0, 0
while ind in range(len(s)):
	if s[ind] == '{':
		temp2 = ind
		ind = s[ind:].find('}')+ind
		print s[temp2:ind+1], ": Comment"
		temp2 = ind + 1
	else:
		if s[ind] == ' ' or s[ind] == ';' or ind == len(s)-1:
			if len(s[temp2:ind]) > 0 or temp2 == len(s) - 1:
				if s[temp2:ind] in KeyWords or s[temp2:] in KeyWords:
					if ind == len(s)-1 and s[ind] != ';':
						print s[temp2:], ": Reserved Word"
					else:
						print s[temp2:ind], ": Reserved Word"
					temp2 = ind + 1
				elif s[temp2:ind] in Symbols or s[temp2:] in Symbols:
					if ind == len(s)-1 and s[ind] != ';':
						print s[temp2:], ": Symbol"
					else:
						print s[temp2:ind], ": Symbol"
					temp2 = ind + 1
				elif '0' <= s[temp2] <= '9':
					if ind == len(s)-1 and s[ind] != ';':
						print s[temp2:], ": Digit"
					else:
						print s[temp2:ind], ": Digit"
					temp2 = ind + 1
				else:
					if ind == len(s)-1 and s[ind] != ';':
						print s[temp2:], ": Identifier"
					else:
						print s[temp2:ind], ": Identifier"
					temp2 = ind + 1
			else:
				temp2 = ind +1
	ind += 1
