Required Python3 Liberaries:
	- matplotlib
	- sklearn
	- mpl_toolkits
	- cv2
	- collections
------------------------
Execution:

Run the following file to estimate the axial map.
	- axial_map.py
------------------------

Files Descriptions:

	- axial_map.py; Uses two eye images with placido rings (one of normal eye as reference and other one of keratoconus eye) and the axial map of keratoconus eye. It extracts the rings/mire points in both the images and find the radius difference for corresponding rings in the two placido ring images. Finally maps the normalized radius difference between reference eye and keratoconus eye to different colors of axial map.
	
	- util_axial.py; All the helper function for axial_map.py is defined in this file.

	- util.py; liberary of helper function for ring identification in placido image.
------------------------
