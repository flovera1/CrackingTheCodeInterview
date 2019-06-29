def inverserList(valLinkedList):
	vReturnList = []
	for i in range(len(valLinkedList),0, -1):
		vReturnList.append(valLinkedList[i-1])

	#print(vReturnList)
	return vReturnList


def checkPalindrome(valLinkedList):
		vReverse = inverserList(valLinkedList)
		
		if (valLinkedList == inverserList(valLinkedList)):
			return True
		else:
			return False


print(checkPalindrome([1,2,1]))


