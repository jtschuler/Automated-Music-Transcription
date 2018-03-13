import numpy as np
import soundfile as sf
import pitch as p
import rhythm as r
import notetable as nt


def getStream():
	filename = 'Eighth Notes.wav'
	tempo = 120
	partitions = 6

	att,rls = r.getAttacks(tempo,partitions,filename)
	att = np.asarray(att)
	rls = np.asarray(rls)
	notes = p.getNotes(tempo,partitions,filename)

	rest = True
	att = np.asarray(att/2, int)
	rls = np.asarray(rls/2, int)

	for i in range(len(notes)):
		if i in att:
			rest = False
		if rest == True:
			notes[i] = 'r'
		if i in rls:
			rest = True


#print(att)
#print(rls)
	print(notes)
	print(nt.toLilyPond(notes))

	score = []
	duration = 1

	for i in range(1,len(notes)):
		if i in att or notes[i-1]!=notes[i]:
			duration = (int) (24/duration + .5)
			if duration != 1:
				duration -= duration % 2
			score.append([notes[i-1],duration])
			duration = 1
		else:
			duration += 1
		
	duration = (int) (24/duration + .5)
	if duration != 1:
		duration -= duration % 2
	score.append([notes[len(notes)-1],duration])

	for i in range(1,len(score)):
		if score[i][1] > 12:
			if score[i-1][1] != 0:
				score[i-1][1] = (int)(1/(1/score[i-1][1]+1/score[i][1]))
			score[i][1] = 0

	for i in range(len(score)-1,0,-1):
		if score[i][1] == 0 or score[i][1] == 12:
			score.pop(i)
		
	temp = score
	score = []

	for i in temp:
		score.append(i[0] + (str)(i[1]))
	print(score)

	stream = score[0]
	for i in range(1, len(score)):
		stream += ' ' + score[i]

	print(stream)
	return stream	
