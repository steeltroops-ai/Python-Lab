st=input("st:")
ls=list(st)
for j in range(len(ls)):
	for i in range(0,len(ls)-1):
	 	if ls[i] > ls[i+1]:
			ls[i], ls[i+1] = ls[i+1], ls[i]
sort_string=''.join(ls)			
print(sort_string)
			
