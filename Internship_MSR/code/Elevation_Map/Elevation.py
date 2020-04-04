import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from mpl_toolkits import mplot3d
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
	rings = [x for _,x in sorted(zip(mean_radius, rings))]

	ring_number = 1
	for points in rings:	
		for radius,theta in points:
			x,y = util.polar2cart(radius, theta)
			x += origin[0]
			y += origin[1]
			temp[int(y), int(x)] = ring_number
		ring_number +=1

	plt.figure()
	plt.imshow(temp)
	plt.show()
	
	return rings

#--------------------------------------------------------------
# This function cleans the input corneal image to get a clean edge map of co-centric rings.
# Uncomment the lines in the function to see the output of each operation.

# Input: Corneal image (in BGR format) with placido reflection.
# Output: returns gray-scale corneal image after enhancing rings and suppressing noise.

def clean_image(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# plt.figure()
	# plt.imshow(gray, cmap='gray')

	# edge_map_initial = cv2.Canny(img,30,55)
	# plt.figure()
	# plt.imshow(edge_map_initial, cmap='gray')

	gausBlur1 = cv2.GaussianBlur(gray, (5,5),0)
	gausBlur2 = cv2.GaussianBlur(gray, (5,5),2)

	difference = gausBlur2-gausBlur1
	# plt.figure()
	# plt.imshow(difference, cmap='gray')

	kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
	output = cv2.morphologyEx(difference, cv2.MORPH_OPEN, kernel_3, iterations=1)
	# plt.figure()
	# plt.imshow(output, cmap='gray')

	final = cv2.medianBlur(output, 5)
	# plt.figure()
	# plt.imshow(final, cmap='gray')

	# final_output = cv2.Canny(final,30,55)
	# plt.figure()
	# plt.imshow(final_output, cmap='gray')
	# plt.show()

	return final

#--------------------------------------------------------------
# Detecting hough circles in the gray scale image.
# This function is to detect innermost circle with a radius range (5pixels-35pixels)

# Input: Gray-scale image of cornea with placido reflection.
# Output: Center (x,y) of co-centric rings.

def detect_circle(img):
	img1 = img.copy()

	detected_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 15, param1 = 55, param2 = 25, minRadius = 5, maxRadius = 35)
	if detected_circles is not None: 
		# Convert the circle parameters a, b and r to integers.
		detected_circles = np.uint16(np.around(detected_circles))

		for pt in detected_circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]
			print('circles detected', a,b,r)

			# Draw the circumference of the circle. 
			cv2.circle(img1, (a, b), r, (100, 255, 0), 1)
	plt.figure()
	plt.imshow(img1)
	plt.show()
	return pt[0],pt[1]


#--------------------------------------------------------------
# Scatter Plot for elevation values at discrete points on the rings.
# Input: Python list, each element(corresponds to each ring) of the list is a 
#        2D array(where first column is radius, second column is Theta) of points on the ring.
# Output: Creates a 3D scattered plot of elevation value.

def scatter_plot(rings, C, origin):
	cart_rings = []
	for points in rings:
		cart_ring = []
		for radius,theta in points:
			x,y = util.polar2cart(radius, theta)
			x += origin[0]
			y += origin[1]
			cart_ring.append((x,y))
		cart_rings.append(np.array(cart_ring).astype('float'))


	fig = plt.figure()
	ax = plt.axes(projection='3d')
	for i in range(len(C)):
		ax.scatter3D(cart_rings[i][:,0], cart_rings[i][:,1], C[i], 'gray')
	plt.show()

#--------------------------------------------------------------

def main():
	filename = '12.png'
	img = cv2.imread(filename)
	gray_img = clean_image(img)
	x_center,y_center = detect_circle(gray_img)
	origin = (x_center, y_center)
	rings = get_rings(gray_img, origin)

	print('number of rings = ', len(rings))
	print('******Number of points on each ring and the mean radius of the ring.*****')
	ring_number =1
	for ring in rings:
		print(ring_number, ring.shape, np.mean(ring[:,0]))
		ring_number +=1
	C = util.predict_elevation_for_rings(rings[:7])
	scatter_plot(rings, C, origin)

#--------------------------------------------------------------
#--------------------------------------------------------------

main()
#--------------------------------------------------------------
