def computeTransition(Pattern,Alphabet,delta) :
	m=len(Pattern)
	n=len(Alphabet)
	for q in range(m+1):
		for a in range(n):
			k=min(m+1,q+2)
			k-=1
			pa=Pattern[:q]+Alphabet[a]
			pk=Pattern[:k]
			
			while not (pa.endswith(pk)) and k>0:
				k-=1
			delta[(Alphabet[a],q)]=k
		#	print(delta)
links=[]
def finiteAutomatonMatcher (Text,delta,m) :
	indices=[]
	n=len(Text)
	q=0
	for i in range (0,n):
		q=delta[(Text[i],q)]
		if q==m :
			print("pattern occurs with shift ",i-m+1)
			k=i-m+1
			indices.append(k)
			while(Text[k] != "\n"):
				k+=1
			links.append("".join(Text[i-m+1:k]))
	loss=0
	for i in indices:
			k=i-loss
			while(Text[k] != "\n"):
				del Text[k]
				loss+=1



'''
with open ("AESOP-TALES.txt", "r") as myfile:
	data=myfile.read()
	
import re
data=re.sub(' +',' ',data)
'''
data=list("http://x.com\n abcd http://n.com\n abcdhtt http//k.com\n")

A=set(data);
Alphabet=list(A);
print(Alphabet)
Pattern=("http");
delta ={}

computeTransition(Pattern,Alphabet,delta)
print(delta)
for (i,q) in delta :
	if delta[(i,q)]>0 :
		print (i,q,delta[(i,q)])
m=len(Pattern)
finiteAutomatonMatcher(data,delta,m)
print(links)
print(data)
