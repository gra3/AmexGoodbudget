filename = "sample.csv"

file = open( filename, "r+" )

lines = file.readlines()

for line in lines:
    length = len( line )
    previousChar = line[ 0 ]
    a = []
    for x in range( 1, length - 1 ):
        if line[ x ] == ',' and line[ x - 1 ] == ',':
            a.append( x - len( a ) )

    for indexToBeDeleted in a:
        line =  line[ :indexToBeDeleted ] + line [ ( indexToBeDeleted + 1 ): ]

    line = line.rstrip()

    lastIndex = len( line ) - 1
    if line[ lastIndex ] == ',':
        line = line[ :-1 ]

    print( line )
    
file.close()
