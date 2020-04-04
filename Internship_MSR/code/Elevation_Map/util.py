import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from mpl_toolkits import mplot3d
import util


theta_neighbour = 0.2
radius_neighbour = 2

min_ring_size = 200 # minimum number of pixels on a ring.
P = 11 # order of zernike polynomial

pixel_size = 0.0014
D = 70# distance between optical center and cornea
focal_length = (4.25 * D)/(D-4.25)

#----------------------------------------------------------------------------
# boolean function returns true when two components lies adjacent to each other on the same ring.
def is_neighbour(component1, component2):
	theta2_min_idx = np.argmin(component2[:,1])
	theta2_max_idx = np.argmax(component2[:,1])

	theta1_min_idx = np.argmin(component1[:,1])
	theta1_max_idx = np.argmax(component1[:,1])

	theta1_min = component1[theta1_min_idx, 1]
	theta1_max = component1[theta1_max_idx, 1]
	radius1_min = component1[theta1_min_idx, 0]
	radius1_max = component1[theta1_max_idx, 0]

	theta2_min = component2[theta2_min_idx, 1]
	theta2_max = component2[theta2_max_idx, 1]
	radius2_min = component2[theta2_min_idx, 0]
	radius2_max = component2[theta2_max_idx, 0]

	if(np.abs(theta1_min-theta2_min) < theta_neighbour):
		if(np.abs(radius1_min-radius2_min) < radius_neighbour):
			return True
	elif(np.abs(theta1_min-theta2_max) < theta_neighbour):
		if(np.abs(radius1_min-radius2_max) < radius_neighbour):
			return True
	elif(np.abs(theta1_max-theta2_min) < theta_neighbour):
		if(np.abs(radius1_max-radius2_min) < radius_neighbour):
			return True
	elif(np.abs(theta1_max-theta2_max) < theta_neighbour):
		if(np.abs(radius1_max-radius2_max) < radius_neighbour):
			return True
	return False


def create_posting_list(polar_components_list):#creates the graph with each component being a node and edge representing two neighboring component on same ring.
	posting_list = [[] for i in range(len(polar_components_list))] #posting list representing graph.
	for i in range(len(polar_components_list)):
		j = 0
		while(j<len(polar_components_list)):
			if(j!=i and is_neighbour(polar_components_list[i], polar_components_list[j])):
				posting_list[i].append(j)
			j +=1
	return posting_list

def DFS(posting_list, visited, idx):
	merge_list = []
	for ele in posting_list[idx]:
		if(not visited[ele]):
			visited[ele] = True
			merge_list.append(ele)
			l,visited= DFS(posting_list, visited, ele)
			merge_list += l
	return merge_list, visited


def merge_components(polar_components_list, merge_list):
	t = tuple(polar_components_list[ele] for ele in merge_list)
	return np.vstack(t)


def cart2polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

def polar2cart(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def get_polar_components(components_list, origin):
	polar_components_list = []
	for component in components_list:
		polar_components_list.append(np.zeros(component.shape).astype('float'))
		for point_itr in range(0,component.shape[0]):
			x,y = component[point_itr,:]
			x -= origin[0]
			y -= origin[1]
			radius, theta = cart2polar(x, y)
			polar_components_list[-1][point_itr,:] = np.array([radius, theta]).astype('float')
	return polar_components_list


def extract_edge_points(edgemap):
	points = []
	row, col = edgemap.shape
	for y in range(row):
		for x in range(col):
			if(edgemap[y,x]!=0):
				points.append((x,y))
	return np.array(points)


def get_connected_components(gray_img):
	edgemap = cv2.Canny(gray_img,30,55)
	edge_points = extract_edge_points(edgemap)
	temp = np.zeros((edgemap.shape))

	clustering = DBSCAN(eps=6, min_samples=10).fit(edge_points)
	distinct_label = set(clustering.labels_) - {-1}
	# print('number of distinct clusters = ', distinct_label)

	components_list = []
	for label in distinct_label:
		idx_clusters = np.where(clustering.labels_ == label)
		components_list.append(edge_points[idx_clusters[0],:])
		for idx in idx_clusters[0]:
			x,y = edge_points[idx,:]
			temp[y,x] = label
	plt.figure()
	plt.imshow(temp)
	# plt.show()
	return components_list

def get_merged_components(polar_components_list):
	posting_list = create_posting_list(polar_components_list)

	visited = [False for i in range(len(polar_components_list))]
	group_components = []
	for i in range(len(polar_components_list)):
		if(not visited[i]):
			visited[i] = True
			merge_list = [i]
			l,visited = DFS(posting_list, visited, i)
			group_components.append(merge_list+l)
	rings = [] #each element is a ring, stored as an array of points.
	for ele in group_components:
		points_on_ring = merge_components(polar_components_list, ele)
		if (points_on_ring.shape[0]>min_ring_size):
			rings.append(points_on_ring)
	return rings


#------------------------------------------------------------------------------------------------
# Regression model trained on calibration data generated through Unity.

def regression_model(radius, l):
	# model[0] = coefficient for ring_number.
	# model[1] = coefficient for (ring_number X elevation_value).
	# model[2] = intercept.
	model = [0.0075656, 0.0045507, -0.03599225377831423]
	elevation = (radius - model[2] - model[0]*l)/model[1]
	return elevation

def predict_elevation_for_rings(rings):
	C = [[] for i in rings]
	l = 1
	for ring in rings:
		for radius,theta in ring:
			# radius has to be in physical length, not in pixels
			radius = (radius * pixel_size)/focal_length
			C[l-1].append(regression_model(radius, l))
		l+=1
	# print('mean Elevation for every ring', [np.mean(c) for c in C])
	return C

#------------------------------------------------------------------------------------------------


