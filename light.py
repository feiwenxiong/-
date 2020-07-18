def light():
	lights =int(input("lights:"))
	raw =input("closeList:")
	raw = raw.replace(" ","" )
	
	closeList = list(map(int,raw))
	
	res=[1]*(lights+1)
	res[0]=0
	
	for close in closeList:
		for i in range(1,lights+1):
			if i%close==0:
				res[i] = 1 - res[i]
	print(sum(res))
	return res

res = light()
print(res)
