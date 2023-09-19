# Function for parsing the numbers
def numberParser(someString):
    output = []
    asList = someString.split(",")
    print(asList)
    for numberSet in asList:
        if len(numberSet) > 2:  # is XY - XZ
            newNumberSet = numberSet.replace(' - ', ",")
            startEnd = newNumberSet.split(",")
            for j in range(len(startEnd)):
                startEnd[j] = int(startEnd[j])
            output.append(startEnd)
        else:  # is a number
            output.append(int(numberSet))
    return output

with open('10 Eastern Area.txt') as f:
    lines = f.readlines()[1:] #Excluding title
    print(lines)

    # Removing line breaks \n
    useList = []
    for line in lines:
       useList.append(line[:-1])
    print(useList)

    #Making a dictionary of postcodes for the region
    postcodes = {}
    for i in range(len(useList)):
        print(useList[i])
        if i % 2 == 0: #is the letter part of postcode
            postcodes[useList[i]] = ""
        else: #is number part of postcode
            postcodeNumber = numberParser(useList[i])
            #Adding to dictionary
            postcodes[useList[i-1]] = postcodeNumber

    print(postcodes)

