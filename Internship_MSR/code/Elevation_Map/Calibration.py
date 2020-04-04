import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


filename = 'CalibrationData.csv' # calibration data file name
pixel_size = 15/451 # pixel size used to calculate the ring radius(in 'mm') in the image plane.
focal_length = 43 # focal length of the pinhole camera used for generation of the calibration data.


datareader = csv.reader(open(filename, "r"), delimiter=",")
temp = next(datareader)
print(temp) # prints the header of the data on the console

Data = []
for row in datareader:
	Data.append(row)
Data=np.array(Data).astype('float')

Data[:,0] = Data[:,0]*(pixel_size/focal_length)#converting ring radius to 'mm' and normalising with focal length

X = Data[:,[1,3]].copy() # To predict the elevation
# X = Data[:,1:3].copy() # To predict the surface radius

X[:,1] = np.multiply(X[:,0],X[:,1]) # create a derived feature as (ring_number X elevation_value).

Y = Data[:,0]
#---------------------------------------------------------------------------------
#Learn regression Model

model = LinearRegression()
model.fit(X,Y)

print('coefficients of model = ',model.coef_)
print('intercept value = ',model.intercept_)
result = model.score(X,Y)
print(result)

#---------------------------------------------------------------------------------
#plot regression function

fig = plt.figure()
ax = plt.axes(projection='3d')

zline = Y
xline = X[:,0]
yline = X[:,1]
ax.scatter3D(xline, yline, zline, 'gray')


xdata = np.linspace(np.min(X[:,0]), np.max(X[:,0]), 1000)
ydata = np.linspace(np.min(X[:,1]), np.max(X[:,1]), 1000)
xdata, ydata = np.meshgrid(xdata, ydata)

zdata = model.predict(np.hstack((xdata.flatten().reshape(-1,1), ydata.flatten().reshape(-1,1))))
zdata = zdata.reshape(xdata.shape)

ax.contour3D(xdata, ydata, zdata, 50)

ax.set_xlabel('Ring number (l)')
ax.set_ylabel('Surface Radius')
ax.set_zlabel('Radius in image plane');

plt.show()
#---------------------------------------------------------------------------------