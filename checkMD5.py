import hashlib
import sys
print 'MD5 reader'
try:
    fileName=sys.argv[1]
except:
    print 'Argomento mancante'
    sys.exit(0)

print fileName
print hashlib.md5(open(fileName,'rb').read()).hexdigest()

