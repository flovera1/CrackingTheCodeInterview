'''
Intuition

Let's record the time dist[node] when the signal reaches the node. 
If some signal arrived earlier, we don't need to broadcast it anymore. 
Otherwise, we should broadcast the signal.

Algorithm

We'll maintain dist[node], the earliest that we arrived at each node. When 
visiting a node while elapsed time has elapsed, if this is the currently-fastest 
signal at this node, let's broadcast signals from this node.

'''


class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in xrange(1, N+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: 
                return
            dist[node] = elapsed
            
            for time, nei in sorted(graph[node]):
            
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1