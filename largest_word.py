st=input("")
new=st.split()
m=n=new[0]
for i in new:
	if len(i)>len(m):
		m=i
	if len(i)<len(n):
		n=i
print('largest is:', m)
print('smallest is:',n)
