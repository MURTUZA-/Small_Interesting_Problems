import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import cv2
import collections
import util_axial

n_bins = 10

#------------------------------------------------------

filename = 'normal_test1.bmp'
img_normal = cv2.imread(filename)

filename = 'test_1.bmp'
img_KT = cv2.imread(filename)
img_size_KT = img_KT.shape[:2]

axial_heatmap = cv2.cvtColor(cv2.imread('test_1_axial.bmp'),cv2.COLOR_BGR2RGB)

gray_img_normal,edgemap_normal = util_axial.clean_image(img_normal)
gray_img_KT,edgemap_KT = util_axial.clean_image(img_KT)

x_center,y_center = util_axial.detect_circle(gray_img_normal)
origin_normal = (x_center, y_center)

x_center,y_center = util_axial.detect_circle(gray_img_KT)
origin_KT = (x_center, y_center)

rings_normal = util_axial.get_rings(edgemap_normal, origin_normal)

# Uncomment below code to use the fixed radii for noraml(reference) eye.
# list_normal = [20, 28, 38, 48, 58, 68, 78, 88, 98, 108]
# ring_itr = 0
# for ring in rings_normal:
# 	if(ring_itr<len(list_normal)):
# 		rings_normal[ring_itr][:,0] = np.array([list_normal[ring_itr] for j in range(len(ring))]).astype('float')
# 	else:
# 		break
# 	ring_itr +=1

rings_KT = util_axial.get_rings(edgemap_KT, origin_KT)

x_list, y_list, normalised_delta_r_list, rgb_list = util_axial.delta_radius(rings_KT[2:10], rings_normal[2:10], img_size_KT, origin_KT, origin_normal, axial_heatmap)
util_axial.cluster_rgb(np.array(normalised_delta_r_list), np.array(rgb_list))

# min_delta_r,bin_size, bin_to_rgb = color_mapping_to_delta_r(normalised_delta_r, Data[:,4:], n_bins)
# for i in range(n_bins):
# 	print(i+1, bin_size*i + min_delta_r, bin_to_rgb[i,:])

# axial_scatter_plot(x_list, y_list, normalised_delta_r_list, img_size_KT, n_bins, bin_size, bin_to_rgb, min_delta_r)

#------------------------------------------------------
