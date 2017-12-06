def outputToFile(fileName, hashList, algorithm):
    with open(fileName, 'w') as f:
        for l in hashList:
            f.write('%s:%s\n' % (algorithm, l))

def fileToList(filename): # takes a file and puts it into an array
    temp = []
    temp = open(filename, 'r').read().split('\n')
    return temp

if __name__ == '__main__':
    source = './' + raw_input('Enter source file (eg source.txt)>')
    destination = './' + raw_input('Enter destination (eg destination.txt)>')
    algorithm = raw_input('Enter algorith used>')

    tempList = fileToList(source)
    outputToFile(destination, tempList, algorithm)
