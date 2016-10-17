import hashlib
import os
def findFile(pathToDir):
	filenames=os.listdir(pathToDir)
	return [filename for filename in filenames if filename.endswith('.py')==False]
print 'MD5 Folder Checker'

path=os.getcwd()
filenames=findFile(path)
for name in filenames:
	try:
		print name,' ' ,hashlib.md5(open(name,'rb').read()).hexdigest()
	except os.error:
		print 'Errore nel tentativo di verificare: ', name
		

