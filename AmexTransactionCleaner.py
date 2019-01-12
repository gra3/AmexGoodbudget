import sys

def clean( filename ):
   transactions = get_transactions(filename)
   print_transactions(transactions)
   saveTransactions( transactions )

def strip_white_space(line):
    line = line.rstrip();
    return line;


def remove_extra_commas(line):
    length = len( line )
    previousChar = line[ 0 ]
    a = []
    for x in range( 1, length - 1 ):
        if line[ x ] == ',' and line[ x - 1 ] == ',':
            a.append( x - len( a ) )

    for indexToBeDeleted in a:
        line =  line[ :indexToBeDeleted ] + line [ ( indexToBeDeleted + 1 ): ]

    return line


def remove_day_of_the_week(line):
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


def get_raw_transactions(filename):
    file = open( filename , "r" )
    lines = file.readlines()
    file.close()
    return lines


def get_transactions(filename):
    result = "";

    lines = get_raw_transactions(filename)
    for line in lines:
        line = remove_extra_commas(line);
        line = strip_white_space(line)
        line = remove_day_of_the_week(line);

        result += line + "\n";

    return result


def print_transactions(transactions):
    print( transactions )


def saveTransactions( transactions ):
    outputFile = open( "output.csv", "w" )
    outputFile.write( transactions )
    outputFile.close()

clean( sys.argv[ 1 ] )