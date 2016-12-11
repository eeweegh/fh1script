
import sys, os, stat

fin = sys.argv[1]

st = os.stat( fin )
count = st[ stat.ST_SIZE ]
extra = count - 4*(count/4)
extra = 4 - extra
print count, extra
if ( count > 4092 ):
	raise RuntimeError( 'script too big' )

fout = 'image.hex'
offset = 0x1D02E000

import intelhex
from intelhex import IntelHex
ih = IntelHex()
ih.loadbin( fin, offset=offset )

for i in range( extra ):
	ih[ offset + count + i ] = 0

ih.write_hex_file( fout )

f = open( fout+".txt", 'w' )

ih = intelhex.IntelHex( fout )
ih.dump( f )

f.close()
