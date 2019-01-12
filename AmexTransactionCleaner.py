import sys

def clean( filename ):
   transactions = getTransactions( filename )
   printTransactions( transactions )
   saveTransactions( transactions )

def stripWhitespace( line ):
    line = line.rstrip();
    return line;


def removeExtraCommas( line ):
    length = len( line )
    previousChar = line[ 0 ]
    a = []
    for x in range( 1, length - 1 ):
        if line[ x ] == ',' and line[ x - 1 ] == ',':
            a.append( x - len( a ) )

    for indexToBeDeleted in a:
        line =  line[ :indexToBeDeleted ] + line [ ( indexToBeDeleted + 1 ): ]

    return line


def removeDayOfTheWeek( line ):
    lastIndex = len( line ) - 1
    if line[ lastIndex ] == ',':
        line = line[ :-1 ]

    splits = line.split( "," )
    date = splits[ 0 ]

    dateSplits = date.split( " " )

    line = dateSplits[ 0 ]
    for x in range( 1, len( splits ) ):
        line = line + "," + splits[ x ]

    return line


def getRawTransactions( filename ):
    file = open( filename , "r" )
    lines = file.readlines()
    file.close()
    return lines


def getTransactions( filename ):
    result = "";

    lines = getRawTransactions( filename )
    for line in lines:
        line = removeExtraCommas( line );
        line = stripWhitespace( line )
        line = removeDayOfTheWeek( line );

        result += line + "\n";

    return result


def printTransactions( transactions ):
    print( transactions )


def saveTransactions( transactions ):
    outputFile = open( "output.csv", "w" )
    outputFile.write( transactions )
    outputFile.close()

clean( sys.argv[ 1 ] )