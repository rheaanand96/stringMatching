def suffix_array(Text):
	n=len(Text)
	x=list(range(n))
	y =[Text[i:n] for i in range(n)]
	return [x for (y,x) in sorted(zip(y,x))]
	

def lcp_array(Text,SA):
	n=len(SA)
	inv_SA=[SA.index(x) for x in range(n)]
	lcp=[]
	for i in range(n-1):
		
sa = suffix_array("banana")
'''
Algorithm 5.11: LCP array construction
Input: text T[0..n], suffix array SA[0..n], inverse suffix array SA-1
[0..n]
Output: LCP array LCP[1..n]
(1) ` ? 0
(2) for i ? 0 to n - 1 do
(3) k ? SA-1
[i] // i = SA[k]
(4) j ? SA[k - 1]
(5) while T[i + `] = T[j + `] do ` ? ` + 1
(6) LCP[k] ? `
(7) if ` > 0 then ` ? ` - 1
(8) return LCP
''
