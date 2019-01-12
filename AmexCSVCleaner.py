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

    splits = line.split( "," )
    date = splits[ 0 ]

    dateSplits = date.split( " " )

    line = dateSplits[ 0 ]
    for x in range( 1, len( splits ) ):
        line = line + ","
        line = line + splits[ x ];

    print( line )
    
file.close()
