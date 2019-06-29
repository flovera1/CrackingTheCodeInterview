'''
Write code to remove duplicates from an unsorted linked list.
'''

def removeDuplicatesFromList(valList):
	vCopy = valList
	for i, vali in enumerate(vCopy):
			vTemp = valList[i]
			vRestOfList = valList[i+1:]
			for j, valj in enumerate(vRestOfList):
				vTemp2 = vRestOfList[j]
				if(vTemp == vTemp2):
					#print(vTemp)
					valList.remove(vTemp)
	return valList
			

print(removeDuplicatesFromList([1, 2, 1, 1, 3]))