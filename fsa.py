def computeTransition(Pattern,Alphabet,delta) :
	m=len(Pattern)
	n=len(Alphabet)
	for q in range(m):
		for a in range(n):
			k=min(m+1,q+2)
			pa=Pattern[:q]+Alphabet[a]
			pk=Pattern[:k]
			k-=1
			while not (pa.endswith(pk)) and k>0:
				k-=1
			delta[(Alphabet[a],q)]=k
		#	print(delta)

def finiteAutomatonMatcher (Text,delta,m) :
	n=len(Text)
	q=0
	for i in range (1,n):
		q=delta[(Text[i],q)]
		if q==m :
			print("pattern occurs with shift ",i-m)

with open ("AESOP-TALES.txt", "r") as myfile:
	data=myfile.read()
	
import re
data=re.sub(' +',' ',data)
#data="httpabcdhttpabcdhtt"
A=set(data);
Alphabet=list(A);
Pattern=("http");
delta ={}
computeTransition(Pattern,Alphabet,delta)
print(delta)
m=len(Pattern)
finiteAutomatonMatcher(data,delta,m)
print(delta)
