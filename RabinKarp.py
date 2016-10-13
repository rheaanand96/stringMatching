def RabinKarpMatcher (T,P,d,q):
	n=len(T)
	m=len(P)
	h=(d**(m-1))%q
	print(h)
	p=0
	t=0
	count=0
	for i in range(m):
		p=(d*p+P[i])%q
		t=(d*t+T[i])%q
		print("p here ",p)
		print("t here ",t)
	for s in range(n-m+1):
		print("t",t)
		print("p",p)
		print("s",s)
		if p==t:
			if P[:m]==T[s:s+m]:
				print("pattern occurs with shift",s)
				count+=1
		if s<(n-m):
				t=(d*(t-T[s]*h)+T[s+m])%q
				print("t now",t)
	return count
data=[1,2,3,4,3,2,4]
A=set(data)
Alphabet=list(A)
print(Alphabet)
Pattern=[2,3]
def RKM(T,P):
	q=13
	d=10
	return RabinKarpMatcher(T,P,d,q)
