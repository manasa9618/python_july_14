a=[1,2,6,8,5,9]
print(a)
for i in a:
	if(i%2==0):
		print(i*10)
	else:
		print(i+10)

#print palindromes

b=[35,56,77,33,565,27,86]
print(b)
for i in b:
	if(str(i)[::-1]==str(i)):
		print(str(i))

#print duplicates and unique values

l=[1,8,2,1,6,5,2,8,57,88,11]
d=[]
u=[]
for i in l:
 if(l.count(i)==1):
    u.append(i)
 else:
    d.append(i)
print("duplicate : ",end="")
print(sorted(set(d)))
print("unique : ",end="")
print(sorted(set(u)))

 
								
								
								
								
								
								
		
		