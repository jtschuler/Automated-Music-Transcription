import numpy as np

def filter(data):
	filtered = np.zeros(len(data))
	for a in range(len(data)):
		temp = np.zeros(5)
		temp[1] = data[a]
		if a - 1 < 0:
			temp[0] = data[a]
		else:
			temp[0] = data[a - 1]
		if a + 1 >= len(data):
			temp[2] = data[a]
		else:
			temp[2] = data[a + 1]
#		if a - 2 < 0:
#			temp[0] = data[a]
#		else:
#			temp[0] = data[a - 1]
#		if a + 2 >= len(data):
#			temp[4] = data[a]
#		else:
#			temp[4] = data[a + 1]
		filtered[a] = np.median(temp)
	return filtered
