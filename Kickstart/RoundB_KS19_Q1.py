
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

	def create_seg_tree(A, l, r, node):
		if l==r:
			node.set_odd_char = set([A[l]])
		else:
			node.left = Node()
			node.right = Node()
			set1 = create_seg_tree(A, l, int(r/2), node.left)
			set2 = create_seg_tree(A, int(r/2)+1, r, node.right)
			node.set_odd_char = set1.union(set2) - set1.intersection(set2)

		node.l_indx = l
		node.r_indx = r
		return node.set_odd_char

	def get_answer(A, l, r, node=self.root):
		if l==node.l_indx:
			if r==node.r_indx:
				return len(node.set_odd_char)
			else:
				if node.left.r_indx > r:
					return get_answer(A, l, r, node.left)
				else:
					set1 = get_answer(A,l,r,node.left)
					set2 = get_answer(A,l,r,node.right)
					return set1.union(set2) - set1.intersection(set2)
		else:
			
