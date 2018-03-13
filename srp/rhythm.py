import numpy as np
import soundfile as sf
from matplotlib import pylab as pl
import extrema as ex
import medianfilter as mf




def attacks(data):
	attacks = [0]
	releases = []
	for i in range(1,len(data)-1):
		if data[i]<data[0]<data[i+1]:
			attacks.append(i)
		if data[i+1]<data[0]<data[i]:
			releases.append(i)
	return attacks,releases

def getAttacks(tempo,partitions,filename):
	data,samplerate = sf.read(filename)
	
	windowsize = 60*samplerate/(tempo*partitions)

	rms = [np.sqrt(np.mean(block**2)) for block in sf.blocks(filename, blocksize=(int)(windowsize), overlap=(int)(windowsize/2))]
	x = np.linspace(0, len(rms)-1, len(rms))
	
#	print(rms)

	rms = mf.filter(rms)
#	pl.show(pl.plot(x,rms))
	
	att,rls = attacks(rms)
	return att,rls
	
#	rest = True
#
#	for i in range(len(rms)):
#		if i in att:
#			rest = False
#		elif i in rls:
#			rest = True
#		if rest == False:
#			rms[i] = 1
#		
#	pl.show(pl.plot(x,rms))
#	print(peaks)
#	return rms,x

def convertRhythm(duration,partitions):
	duration = (int) (partitions*4/duration + .5)
	return duration
	
def convertStream(data):
	for i in range(len(data)):
		data[i][1] = convertRhythm(data[i][1])
		
