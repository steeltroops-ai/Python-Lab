st=input()
m=st[0]
for ch in st:
	if ch < m:
		m=ch
		
		print('min char in string',m)
