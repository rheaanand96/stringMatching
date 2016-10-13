def computeOccurrences(inTextRange,Pattern,Algo):
	start = inTextRange(0)
	end = inTextRange(1)
	Text=data[start:end]
	count=Algo(Text,Pattern)
	return count
