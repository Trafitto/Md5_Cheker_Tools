import hashlib
import os
import sys
def findFile(pathToDir):
	filenames=os.listdir(pathToDir)
	return [filename for filename in filenames if filename.endswith('.py')==False]
print 'MD5 Folder Finder- Find the file with MD5 checsums'
print 'FindMD5_Folder.py <MD5 to find>'
try:
    md5ToSeek=sys.argv[1]
except:
    print 'Argomento mancante'
    sys.exit(0)

isFinded=False
path=os.getcwd()
filenames=findFile(path)
for name in filenames:
	try:
		scanMd5=hashlib.md5(open(name,'rb').read()).hexdigest()
		if scanMd5==md5ToSeek:
			print 'File trovato!!'
			print name, ' ' ,scanMd5
			isFinded=True
	except os.error:
		print 'Errore nel tentativo di verificare: ', name
if isFinded==False:
	print 'Nessun file trovato'
	