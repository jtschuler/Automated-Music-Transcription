

notes = ['C0','Db0','D0','Eb0','E0','F0','Gb0','G0','Ab0','A0','Bb0','B0','C1','Db1','D1','Eb1','E1','F1','Gb1','G1','Ab1','A1','Bb1','B1','C2','Db2','D2','Eb2','E2','F2','Gb2','G2','Ab2','A2','Bb2','B2','C3','Db3','D3','Eb3','E3','F3','Gb3','G3','Ab3','A3','Bb3','B3','C4','Db4','D4','Eb4','E4','F4','Gb4','G4','Ab4','A4','Bb4','B4','C5','Db5','D5','Eb5','E5','F5','Gb5','G5','Ab5','A5','Bb5','B5','C6','Db6','D6','Eb6','E6','F6','Gb6','G6','Ab6','A6','Bb6','B6','C7','Db7','D7','Eb7','E7','F7','Gb7','G7','Ab7','A7','Bb7','B7','C8','Db8','D8','Eb8','E8','F8','Gb8','G8','Ab8','A8','Bb8','B8']

a4=440.00

nt = []
note = a4/((2**(1/12))**58)

for a in range(len(notes)):
	note *= 2**(1/12)
	nt.append([int(note*100+.5)/100,notes[a]])
	
	
ftn = {a4: 'A4'}
ntf = {'A4': a4}

for a in range(len(nt)):
	ntf[nt[a][1]]=nt[a][0]
	ftn[nt[a][0]]=nt[a][1]

ftn[0.00] = 'r'


def matchFrequency(freq):
	match = sorted(ftn.keys())
	index = 0
	for i in range(len(match)):
		if(abs((match[i]-freq)**2)<abs((match[index]-freq)**2)):
			index = i
	return match[index]
	
def toly(s):
	s = s.replace('1', ',,')
	s = s.replace('2', ',')
	s = s.replace('3', '')
	s = s.replace('4', '\'')
	s = s.replace('5', '\'\'')
	s = s.replace('6', '\'\'\'')
	s = s.replace('7', '\'\'\'\'')
	s = s.replace('8', '\'\'\'\'\'')
	s = s.replace('b', 'es')
	s = s.replace('#', 'is')
	s = s.lower()
	return s
def toLilyPond(notes):
	for i in range(len(notes)):
		notes[i] = toly(notes[i])
	return notes
