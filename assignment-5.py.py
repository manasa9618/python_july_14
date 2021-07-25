p="hello manasa.\n this is python programming.\nr you intrested manasa."
word=p.split()
largest=small=word[0]
for i in range(0,len(word)):
    if(len(largest)<len(word[i])):
       largest=word[i]
    if(len(small)>len(word[i])):
       small=word[i]
print("largest word in string ",largest)
print("smallest word is ",small)


#largest word in every sentence

w=p.split("\n")
for j in range(0,len(w)):
 l=w[j].split()[0]
 for i in (w[j].split()):
  if(len(i)>len(l)):
    l=i
 print(l)
            

#shortest word in every sentence

 w=p.split("\n")
for j in range(0,len(w)):
 l=w[j].split()[0]
 for i in (w[j].split()):
  if(len(i)<len(l)):
    l=i
 print(l)
            
