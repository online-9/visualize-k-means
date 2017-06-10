from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import random
from six.moves import input

def plotme(data, target, centroids=[], legends=False, iter=None):
	plt.clf()


	class_1 = data[target==0]
	class_2 = data[target==1]
	class_3 = data[target==2]


	
	if legends:
		c1 = plt.scatter(class_1[:,0], class_1[:,1],c='m',
			    marker='+')
	
		c2 = plt.scatter(class_2[:,0], class_2[:,1],c='m',
			    marker='o')
	

		c3 = plt.scatter(class_3[:,0], class_3[:,1],c='m',
			    marker='*')
		plt.legend([c1, c2, c3], ['Setosa', 'Versicolor',
	    			'Virginica'])
		plt.title('Iris dataset with 3 clusters and known outcomes')
	else:
		c1 = plt.scatter(class_1[:,0], class_1[:,1],c='r',
			    marker='+')
	
		c2 = plt.scatter(class_2[:,0], class_2[:,1],c='g',
			    marker='o')
	

		c3 = plt.scatter(class_3[:,0], class_3[:,1],c='b',
			    marker='*')
		if centroids!=[]:
			plt.scatter(centroids[:,0],centroids[:,1],c='k',marker='x')
		plt.title('Iris dataset with 3 clusters and unknown outcomes : Iter '+str(iter))
	
	plt.pause(2)

def euclidian(x1,x2):
	return (np.sum((x1-x2)**2))

def getclass(datapoint, centroids):
	distances = np.array([euclidian(datapoint, centroid) for centroid in centroids])
	return np.argmin(distances)


def compute_centroids(data, centroids):
	classes = np.zeros(data.shape[0])
	for i in range(len(data)):
		classes[i] = getclass(data[i], centroids)
	new_centroids = np.ndarray(centroids.shape)

	for i in range(len(centroids)):
		new_centroids[i] = np.mean(data[classes==i],axis=0)


	return new_centroids, classes



def kmeans(data, targets, k=2, iters=10,plotdata=None):


	centroids = random.sample(range(data.shape[0]),k)
	print(centroids)
	centroids =  np.array([data[i] for i in centroids])

	for iter in range(iters):
		centroids, classes = compute_centroids(data, centroids)
		plotme(plotdata,classes, centroids, iter=iter+1)

	plotme(plotdata, targets, centroids, legends=True)
	input("Press any key to continue:")
	plotme(plotdata, classes, iter="Final")
	input("Press any key to exit:")

if __name__ == '__main__':

	iris = load_iris()

	# Reduce iris data from 4 dimensionsto 2 for ease of plotting

	pca = PCA(n_components=2).fit(iris.data)
	pca_2d = pca.transform(iris.data)
	plt.ion()
	
	#You can change the first argument to iris.data and remove the centroid argument in every plotme call
	kmeans(pca_2d, iris.target, k=len(np.unique(iris.target)), plotdata=pca_2d)
