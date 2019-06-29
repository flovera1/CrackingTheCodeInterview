'''
IS NOT READY!





There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

'''
def cheapestFlightBFS(numberOfNodes, flights, src, dst, k):
	graph = []


	for s, d, p in flights:
		graph.append([s,d,p])
	print(graph)

	
	queue = [(0, src, k)]

	
	while(len(queue)>0):
		returnWeight, tempSrc, tempRemainingSteps = queue.pop()

		print(tempSrc)
		if tempSrc == dst:
			return returnWeight

		if tempRemainingSteps > 0:
			for stop in graph:
				#if (stop[1] == tempSrc):

				queue.append((returnWeight+stop[2], stop[1], tempRemainingSteps-1))



print(cheapestFlightBFS(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 2))
