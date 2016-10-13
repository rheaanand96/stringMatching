def computeTransition(Pattern,Alphabet) :
	m=len(Pattern)
	n=len(Alphabet)
	delta{}
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
	return delta

def finiteAutomatonMatcher (Text,delta,m) :
	links=[]
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



def FSA (T,P):
	A=set(T);
	Alphabet=list(A);
	print(Alphabet)
	Pattern=("http");
	delta=computeTransition(Pattern,Alphabet)
	print(delta)
	for (i,q) in delta :
		if delta[(i,q)]>0 :
			print (i,q,delta[(i,q)])
	m=len(Pattern)
	links=finiteAutomatonMatcher(data,delta,m)
	print(links)
	print(data)
