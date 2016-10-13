def suffix_array(Text):
	n=len(Text)
	x=list(range(n))
	y =[Text[i:n] for i in range(n)]
	A = [x for (y,x) in sorted(zip(y,x))]
	print(A)
	return A

def lcp(T,SA):
	l=0
	n=len(SA)
	lcp=[0]*n
	for i in range(n):
		k=SA.index(i) 
		j=SA[k-1]
		while  j<n-l and T[i+l]==T[j+l] :
			print("i,j,l: ",i,j,l)
			l+=1
		lcp[k]=l
		if l>0:
			l=l-1
		print("lcp: ",lcp)
	print("lcp: ",lcp)
	return lcp
	
def Search (Pattern,Text,SA):
	n=len(Text)
	m= len(Pattern)
	l=0
	r=n-1
	while l<=r :
		print(r)
		print(l)
		mid = l+(r-l)/2
		print(mid,SA[mid],m)
		#print(Text[4:m+1])
		res = Pattern==Text[SA[mid]:SA[mid]+m]
		print("pa",Pattern,"txt",Text[SA[mid]:SA[mid]+m])
		if res==1:
			print("pattern found at index ",SA[mid])
			return
		elif Pattern < Text[SA[mid]:SA[mid]+m] :
			r=mid-1
		else :
			l=mid+1
	print("pattern not found")
	
	
T="bnnana"
P="ana"
SA = suffix_array(T)
lcp(T,SA)
Search(P,T,SA)
