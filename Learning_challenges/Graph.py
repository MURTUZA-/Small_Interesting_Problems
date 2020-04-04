from collections import deque
import sys
filename = sys.argv[1]

queue = deque([])

# class queue:
# 	def __init__():
# 		front = -1
# 		rear = -1
# 		L = []
# 	def pop():
# 		if front==rear
# 		temp = L[front]
# 		L.pop(front)
# 		front++
# 		return temp

def BFS(Graph,V, v):
	visited = {i+1:False for i in range(V)}
	queue.append(v)
	endline_count = len(queue)
	for ele in queue:
		if endline_count==1:
			print(ele)
			endline_count = len(queue)
		else:
			print(ele, end=' ')
			endline_count -=1
		visited[ele]=True
		queue.popleft()
		for v,w in Graph[ele]:
			if not visited[v]:
				queue.append(v)


file = open(filename, 'r')
V = int(file.readline())
for 
V = int(input('enter number of vertices in the graph'))
Grpah = {i+1:[] for i in range(V)}
E = int(input('enter number of edges in the graph'))
print('enter edges one by one along with corresponding edge weight e.g. (v1,v2, w), v1 and v2 are unordered.')
for e in range(E):
	v1,v2,w = [int(ele) for ele in input().split()]
	Graph[v1].append((v2,w))
	Graph[v2].append((v1,w))
BFS(Graph, V, 1)


