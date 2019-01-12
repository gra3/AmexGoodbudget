import sys

def StripWhitespace( line ):
    line = line.rstrip();
    return line;

def RemoveExtraCommas( line ):
    length = len( line )
    previousChar = line[ 0 ]
    a = []
    for x in range( 1, length - 1 ):
        if line[ x ] == ',' and line[ x - 1 ] == ',':
            a.append( x - len( a ) )

    for indexToBeDeleted in a:
        line =  line[ :indexToBeDeleted ] + line [ ( indexToBeDeleted + 1 ): ]

    return line

def RemoveDayOfTheWeek( line ):
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

def GetRawTransactions():
    file = open( sys.argv[ 1 ] , "r+" )
    lines = file.readlines()
    file.close()
    return lines

def GetTransactions():
    result = "";

    lines = GetRawTransactions()
    for line in lines:
        line = RemoveExtraCommas( line );
        line = StripWhitespace( line )
        line = RemoveDayOfTheWeek( line );

        result += line + "\n";

    return result

def SaveTransactions( transactions ):
    outputFile = open( "output.csv", "w" )
    outputFile.write( result )
    outputFile.close()


result = GetTransactions();

print( result )

SaveTransactions( result );
