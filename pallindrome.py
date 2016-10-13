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
	
def findlpallin(mtxt,LCP,l,SA) :
	llength=0
	position=0
	for i in range(1,len(mtxt)):
		if(LCP[i]>llength):
			if(SA[i-1]<l and SA[i]>l or SA[i]<l and SA[i-1]>l):
				print("calculating longest SA[i-1] & SA[i]")
				llength=LCP[i]
				position=SA[i]
	print("longest pallin length",llength)
	print("longest pallindrom",mtxt[position:position+llength])
	
T="malayalam"
l=len(T)
mtxt= T+'#'+T[::-1]
SA = suffix_array(mtxt)
LCP=lcp(mtxt,SA)
findlpallin(mtxt,LCP,l,SA) 
#Search(P,T,SA)
'''
def findlpallin(mtxt,lcp,l,SA,lcp) :
	llength=0
	position=0
	for i in range(1,len(mtxt)):
		if(lcp[i]>llength):
			if(lcp[i]>llength):
				if(SA[i-1]<l and SA[i]>l||SA[i]<l and SA[i-1]>l):
					print("calculating longest SA[i-1] & SA[i]")
					llength=lcp[i]
					position=SA[i]
	print("longest pallin length",llen)
	print("longest pallindrom",mtxt[pos:pos+llen])
	
Let the length of the Longest Palindrome ,longestlength:=0 (Initially)
    Let Position:=0
    for(int i=1;i<Len;++i)
    {
        //Note that Len=Length of Original String +"#"+ Reverse String
        if((LCP[i]>longestlength))
        {
            //Note Actual Len=Length of original Input string .
            if((suffixArray[i-1]<actuallen && suffixArray[i]>actuallen)||(suffixArray[i]<actuallen && suffixArray[i-1]>actuallen))
            {
                 //print :Calculating Longest Prefixes b/w suffixArray[i-1] AND  suffixArray[i]


                longestlength=LCP[i];
              //print The Longest Prefix b/w them  is ..
              //print The Length is :longestlength:=LCP[i];
                Position=suffixArray[i];
            }
        }
    }
    So the length of Longest Palindrome :=longestlength;
    and the longest palindrome is:=Str[position,position+longestlength-1];

void search(char *pat, char *txt, int *suffArr, int n)
{
    int m = strlen(pat);  // get length of pattern, needed for strncmp()
 
    // Do simple binary search for the pat in txt using the
    // built suffix array
    int l = 0, r = n-1;  // Initilize left and right indexes
    while (l <= r)
    {
        // See if 'pat' is prefix of middle suffix in suffix array
        int mid = l + (r - l)/2;
        int res = strncmp(pat, txt+suffArr[mid], m);
 
        // If match found at the middle, print it and return
        if (res == 0)
        {
            cout << "Pattern found at index " << suffArr[mid];
            return;
        }
 
        // Move to left half if pattern is alphabtically less than
        // the mid suffix
        if (res < 0) r = mid - 1;
 
        // Otherwise move to right half
        else l = mid + 1;
    }
 
    // We reach here if return statement in loop is not executed
    cout << "Pattern not found";
}
	
'''	


