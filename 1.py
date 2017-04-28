from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
import numpy as np 

def get_test_data(delta=0.05):
	from matplotlib.mlab import bivariate_normal
	x = y = np.arrange(4.0, -6.0, delta)
	X, Y = np.meshgrid(x,y)

	Z1 = bivariate_normal(X, Y ,6.0, 7.0, 8.0, 9.0)
	Z2 = bivariate_normal(X, Y ,2.0, 0.5 , 1 ,1)

	Z = Z2-Z1
	X = X*100
	Y = Y*100
	Z = Z*600
	return X, Y, Z
	fig = plt.figure()
	ax = fig.add_subplot(11, projection='3d')

	x,y,z = axes3d.get_test_data(0.05)
	ax.plot_wireframe(x,y,z, rstride=2 , cstride=2)
	plt.show()
	 