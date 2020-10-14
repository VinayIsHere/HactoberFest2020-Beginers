#!/usr/bin/env python3
#by vinayk9119
def sortString(str): 
    return ''.join(sorted(str))

for _ in range(int(input())):
	s=input()
	p=input()
	s=list(sortString(s))
	for i in p:
		s.remove(i)
	s=''.join(map(str,s))
	if(p[0] in s):
		index=s.rindex(p[0])
	else:
		temp=p[0]
		try:
			while(not(temp in s)):
				temp=chr(ord(temp)-1)
			index=s.rindex(temp)
		except:
			index=-1
	s=s[:index+1]+p+s[index+1:]
	print(s)
