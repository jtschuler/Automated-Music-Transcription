import numpy as np
import soundfile as sf
import math
import pylab as pl
import medianfilter as mf
import extrema as ex
import notetable as nt

lownote = 'Bb1'									#lower bound
lowfreq = nt.ntf[lownote]

def getPitch(data,samplerate):
	data = np.fft.fft(data)
	frequencies = np.linspace(0, samplerate/2, len(data)/2)

	data = abs(data**2)

	data=data[:int(len(data)/2)]

	#data = mf.filter(data)

	peaks = ex.findPeaks(data)
	next_iter = ex.findPeaksIndices(data, peaks)
	while len(peaks)>100:
		if len(next_iter)>0:
			peaks = next_iter
		else:
			break
		next_iter = ex.findPeaksIndices(data, peaks)

	freq = 0

	for i in range(len(peaks)-3):
		if abs(peaks[i] * 2 - peaks[i+1]) < 100 or abs(peaks[i] * 3 - peaks[i+1]) < 100 or abs(peaks[i] * 4 - peaks[i+1]) < 100:
			#if abs(peaks[i] * 3 - peaks[i+2]) < 100 or abs(peaks[i] * 4 - peaks[i+2]) < 100 or abs(peaks[i] * 5 - peaks[i+2]) < 100:
			if frequencies[peaks[i]] >= lowfreq:
				freq = frequencies[peaks[i]]
				break
		
	#print (freq)
	freq = nt.matchFrequency(freq)
	#print (nt.ftn[freq])
	return nt.ftn[freq]





def getNotes(tempo,partitions,filename):
	data,samplerate = sf.read(filename)
	windowsize = (int)(60*samplerate/(tempo*partitions))

	try:
		data=np.swapaxes(data,0,1)
		data=data[0]
	except TypeError:
		data=data
	
	#data = mf.filter(data)
	data -= np.mean(data)
	notes = []
	for i in range(int(len(data)/windowsize)):
		lowerbound = i*windowsize
		upperbound = (i+1)*windowsize
		if upperbound >= len(data):
			upperbound = len(data)-1
		notes.append(getPitch(data[lowerbound:upperbound],samplerate))
		
	return notes
