
class Node:
	def __init__(self):
		self.set_odd_char = set()
		self.l_indx = 0
		self.r_indx = 0
		self.left = None
		self.right = None

class SegTree:
	def __init__(self):
		self.root = Node()

	def create_seg_tree(self, A, l, r, node):
		if l==r:
			node.set_odd_char = set([A[l]])
		else:
			node.left = Node()
			node.right = Node()
			set1 = self.create_seg_tree(A, l, int(r/2), node.left)
			set2 = self.create_seg_tree(A, int(r/2)+1, r, node.right)
			node.set_odd_char = set1.union(set2) - set1.intersection(set2)

		node.l_indx = l
		node.r_indx = r
		return node.set_odd_char

	def get_answer(self, l, r, node):

		if l==node.l_indx:
			if r==node.r_indx:
				return node.set_odd_char
			else:
				if node.left.r_indx >= r:
					return self.cget_answer(l, r, node.left)
				else:
					set1 = self.get_answer(l, node.left.r_indx, node.left)
					set2 = self.get_answer(node.left.r_indx+1, r, node.right)
					return set1.union(set2) - set1.intersection(set2)
		else:
			if l>=node.right.l_indx:
				return self.get_answer(l, r, node.right)
			else:
				if r<=node.left.r_indx:
					return self.get_answer(l, r, node.left)
				else:
					set1 = self.get_answer(l, node.left.r_indx, node.left)
					set2 = self.get_answer(node.left.r_indx+1, r, node.right)
					return set1.union(set2) - set1.intersection(set2)

			
T = int(input())
for itr in range(T):
	N,Q = [int(ele) for ele in input().split()]
	blocks = input()

	tree = SegTree()
	tree.create_seg_tree(blocks, 0, N-1, tree.root)
	
	count = 0
	for q in range(Q):
		l,r = [int(ele)-1 for ele in input().split()]
		temp = tree.get_answer(l, r, tree.root)
		if len(temp)==0:
			count+=1
	print('Case #'+str(itr+1)+': '+str(count))