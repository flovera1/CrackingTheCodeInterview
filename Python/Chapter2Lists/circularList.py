from linkedList import LinkedList

_set 	= set()

def loopDetection(valMyList):
	vValue = None

	for i in valMyList:
		if not(i.value in _set):
			_set.add(i.value)
		else:
			vValue = i.value
			break	

	return vValue



_list =  LinkedList()
_list.addSeveral(["A", "B", "C", "D", "E", "C"])
print(loopDetection(_list))
