import ScoreData as sd
import subprocess as sp

stream = sd.getStream()
filename = 'test'

f = open(filename + '.ly',"w+")

f.write('\\version \"2.18.2\"\n')
f.write('{\n\t\\absolute\n')

f.write("\t" + stream)

f.write('\n}\n')
f.close()

sp.run(["lilypond", filename + ".ly"])
sp.run(["google-chrome", filename + ".pdf"])
