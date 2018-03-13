import numpy as np

def findPeaks(array):										#Find local maxes
	peaks = []
	peaks.append(0)
	for i in range(10,len(array)-11):
		if array[i-10] < array[i] > array[i+10]:
			peaks.append(i)
	peaks.append(len(array)-1)
	return peaks
	
def findPeaksIndices(array, indices):							#Find local maxes using indices instead of actual values
	peaks = []
	peaks.append(indices[0])
	values = []
	for i in range(len(indices)):
		values.append(array[indices[i]])
		
	for j in range(1,len(indices)-1):
		if values[j-1] < values[j] > values[j+1]:
			peaks.append(indices[j])
	peaks.append(indices[len(indices)-1])
	return peaks

def findMins(array):										#Find local mins
	peaks = []
	peaks.append(0)
	for i in range(10,len(array)-11):
		if array[i-10] > array[i] < array[i+10]:
			peaks.append(i)
	peaks.append(len(array)-1)
	return peaks
	
def findMinsIndices(array, indices):							#Find local mins using indices instead of actual values
	peaks = []
	peaks.append(indices[0])
	values = []
	for i in range(len(indices)):
		values.append(array[indices[i]])
		
	for j in range(1,len(indices)-1):
		if values[j-1] > values[j] < values[j+1]:
			peaks.append(indices[j])
	peaks.append(indices[len(indices)-1])
	return peaks


def getExtrema(array):										#Find local mins
	return findMins(array), findPeaks(array)
	
def getExtremaIndices(array, indices):										#Find local mins
	return findMins(array, indices), findPeaks(array, indices)
	
def getValues(array,data):
	vals = np.zeros(len(array))
	for i in range(len(array)):
		vals[i]= data[array[i]]
	return vals
