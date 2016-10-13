def KMPMatcher(T,P):
	n=len(T)
	m=len(P)
	pi=ComputePrefixFunction(P)
	print("hi")
	q=0
	count=0
	for i in range (1,n+1):
		while q>0 and P[q]!=T[i-1]:
			q=pi[q]
		if P[q]==T[i-1]:
			q=q+1
		if q==m:
			print ("Pattern occurs with shift",i-m)
			count+=1
			q=pi[q]
	return count

def ComputePrefixFunction(P) :
	m=len(P)
	pi=[0]*(m+1)
	pi[1]=0
	k=0
	for q in range(2,m+1):
		print(q)
		while k>0 and P[k]!=P[q-1] :
			k=pi[k]
		if P[k]==P[q-1]:
			k=k+1
		pi[q]=k
		print("pi",pi)
	return pi
data=list("ababacabbababacacacabacac")

A=set(data);
Alphabet=list(A);
print(Alphabet)
Pattern=("ababaca");
KMPMatcher(data,Pattern)

