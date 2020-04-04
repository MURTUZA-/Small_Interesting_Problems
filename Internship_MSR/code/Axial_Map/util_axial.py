import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import collections
import util

#--------------------------------------------------------------
# This is the function to assign each point on the ring, the label(ring number).
# First element in the output list is corresponding to innermost ring, and last corresponding to outermost ring.

# Input: Gray-scale corneal image and the coordinate of center of the co-centric rings.
# Output: A python List, where ith element of this list is a 2D-array of coordinates of points on the ith ring.

def get_rings(gray_img, origin):
	components_list = util.get_connected_components(gray_img)
	polar_components_list = util.get_polar_components(components_list, origin)
	rings = util.get_merged_components(polar_components_list)

	temp = np.zeros((gray_img.shape))
	mean_radius = []
	for points in rings:
		mean_radius.append(np.mean(points[:,0]))
	rings = [x for _,x in sorted(zip(mean_radius, rings))] #order the rings based on average ring radius

	ring_number = 1
	for points in rings:	
		for radius,theta in points:
			x,y = polar2cart(radius, theta)
			x += origin[0]
			y += origin[1]
			temp[int(y), int(x)] = (ring_number%2)*50+50
		ring_number +=1

	plt.figure()
	plt.imshow(temp)
	plt.show()
	
	return rings

def polar2cart(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y
#----------------------------------------------------------------

def temp_erase_edge_points(edgemap):
	points_KT = [(285,226), (299,226), (294, 226), (304,225), (285,203), (289,204), (294,204)]
	n=4
	for x,y in points_KT:
		x_min = x-n
		x_max = x+n
		y_min = y-n
		y_max = y+n
		edgemap[y_min:y_max, x_min:x_max]=0
	return edgemap


def clean_image(img):#returns edgemap after cleaning of image.
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# plt.figure()
	# plt.imshow(gray, cmap='gray')

	# edge_map_initial = cv2.Canny(img,30,60)
	# plt.figure()
	# plt.imshow(edge_map_initial, cmap='gray')

	gausBlur1 = cv2.GaussianBlur(gray, (5,5),10)

	difference = gray-gausBlur1
	enhanced_gray = 2*difference+gray

	bilateral = cv2.bilateralFilter(enhanced_gray, 15, 75, 75)

	# plt.figure()
	# plt.imshow(bilateral, cmap='gray')

	kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
	output = cv2.morphologyEx(bilateral, cv2.MORPH_OPEN, kernel_3, iterations=1)
	output = cv2.morphologyEx(output, cv2.MORPH_CLOSE, kernel_3, iterations=1)
	# plt.figure()
	# plt.imshow(output, cmap='gray')

	gausBlur2 = cv2.GaussianBlur(output, (5,5),10)
	output = output-gausBlur2


	final = cv2.medianBlur(output, 5)
	final = cv2.medianBlur(final, 5)
	# plt.figure()
	# plt.imshow(final, cmap='gray')


	final_output = cv2.Canny(final,30,55)
	final_output = temp_erase_edge_points(final_output)
	# plt.figure()
	# plt.imshow(final_output, cmap='gray')
	# plt.show()

	return final, final_output

#--------------------------------------------------------------
# Detecting hough circles in the gray scale image.
# This function is to detect innermost circle with a radius range (5pixels-35pixels)

# Input: Gray-scale image of cornea with placido reflection.
# Output: Center (x,y) of co-centric rings.

def detect_circle(img):#Detecting hough circles in the gray scale image.
	# gray_blurred = cv2.blur(img, (3, 3))
	img1 = img.copy()
	pt0=0
	pt1=0
	detected_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 15, param1 = 55, param2 = 10, minRadius = 8, maxRadius = 15)
	if detected_circles is not None: 
		# Convert the circle parameters a, b and r to integers.
		detected_circles = np.uint16(np.around(detected_circles))

		for pt in detected_circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]
			pt0 = a
			pt1 = b
			print('circles detected', a,b,r)

			# Draw the circumference of the circle. 
			cv2.circle(img1, (a, b), r, (100, 255, 0), 2)
			break
	plt.figure()
	plt.imshow(img1)
	plt.show()
	return pt0,pt1
#--------------------------------------------------------------


#------------------------------------------------------
# Compares the rings radius in two images at same theta.
def delta_radius(rings_KT, rings_normal, img_size_KT, origin_KT, origin_normal, axial_heatmap):
	color_map = np.zeros((img_size_KT[0],img_size_KT[1],3))
	ring_number = 1
	x_list = []
	y_list = []
	normalised_delta_r_list = []
	rgb_list = []

	Data = []
	for ring in rings_KT:
		for r_KT,theta in ring:
			idx = np.abs(rings_normal[ring_number-1][:,1]-theta).argmin()
			r_normal = rings_normal[ring_number-1][idx,0]

			delta_r = r_KT-r_normal
			normalised_delta_r = np.round(delta_r/r_normal,2)
			if(normalised_delta_r>=1.7):
				print(ring_number, r_normal, r_KT, theta)

			x,y = polar2cart(r_KT, theta)
			x = int(x + origin_KT[0])
			y = int(y + origin_KT[1])
			
			data_point = (x,y, normalised_delta_r, r_normal, axial_heatmap[y,x,0], axial_heatmap[y,x,1], axial_heatmap[y,x,2])

			if(not ((data_point[4]==0 and data_point[5]==0 and data_point[6]==0) or (data_point[4]==255 and data_point[5]==255 and data_point[6]==255))):
				x_list.append(x)
				y_list.append(y)

				normalised_delta_r_list.append(normalised_delta_r)
				rgb_list.append((data_point[4], data_point[5], data_point[6]))

				Data.append(data_point)
		ring_number+=1

	# np.savetxt("Delta_radius_axial_map.csv", np.array(Data), delimiter=",", fmt='%3.2f')
	return x_list, y_list, normalised_delta_r_list, rgb_list
#------------------------------------------------------

# Does the clustering of the same pixel values and plots frequency of delta_r values for each cluster(rgb value).
def cluster_rgb(delta_r, rgb):
	db = DBSCAN(eps=0.1, min_samples=1).fit(rgb)
	labels = db.labels_
	delta_r_for_each_cluster = []
	rgb_for_each_cluster = []
	for label in set(labels):
		idx = np.where(np.array(labels)==label)
		idx = list(idx[0])
		rgb_for_each_cluster.append(rgb[idx,:])
		delta_r_for_each_cluster.append(delta_r[idx])		
	
	# printing pixel value and its frequency.
	itr =0
	for rgb_list in rgb_for_each_cluster:
		if(len(rgb_list)>10):
			r_arr = np.array(delta_r_for_each_cluster[itr])
			freq = collections.Counter(r_arr)
			print(rgb_list[0], len(rgb_list))

			value = []
			occurance = []
			for ele in freq:
				value.append(ele)
				occurance.append(freq[ele])
			plt.figure()
			plt.stem(value, occurance)
			plt.xticks(np.arange(-0.4, 0.02, .05))
			print('-------------------------------')
		itr+=1

	plt.show()

#------------------------------------------------------
def color_mapping_to_delta_r(delta_r, rgb, n_bins):
	min_delta_r = np.min(delta_r)
	max_delta_r = np.max(delta_r)
	bin_size = (max_delta_r-min_delta_r)/n_bins
	bin_to_rgb = np.zeros((n_bins,3)).astype('float')

	for i in range(n_bins):
		first = bin_size*i + min_delta_r
		last = first+ bin_size
		idx = np.where(np.logical_and(delta_r>=first, delta_r<last))
		idx = list(idx[0])
		bin_to_rgb[i,:] = np.mean(rgb[idx,:], axis=0)
	return min_delta_r,bin_size, bin_to_rgb

#------------------------------------------------------
def axial_scatter_plot(x_list, y_list, delta_r_list, img_size_KT, n_bins, bin_size, bin_to_rgb, min_delta_r):
	rgb_list = []
	itr = 0
	x_arr = np.array(x_list)
	y_arr = np.array(y_list)
	for itr in range(len(x_list)):
		delta_r = delta_r_list[itr]
		bin_idx = int((delta_r - min_delta_r)/bin_size)
		if(bin_idx>=0 and bin_idx<bin_to_rgb.shape[0]):
			rgb_list.append(bin_to_rgb[bin_idx,:])
		else:
			rgb_list.append(np.array([0,0,0]))
	plt.figure()
	plt.imshow(img_KT)
	plt.scatter(x_arr,y_arr, c=np.array(rgb_list)/255, s=50)
	plt.show()

#------------------------------------------------------
#------------------------------------------------------