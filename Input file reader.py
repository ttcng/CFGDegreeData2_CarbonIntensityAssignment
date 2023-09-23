# Function for parsing the numbers
def townParser(someString, region, areaID):
    townToRegion = {}
    asList = someString.split(", ")
    print(asList)
    for town in asList:
        townToRegion[town] = {'region': region,
                              'areaID': areaID}
    return townToRegion

with open('townsData/10 Eastern Area.txt') as f:
    lines = f.readlines() #Excluding title
    print(lines)

    useList = []
    for line in lines:
       useList.append(line[:-1])

    region = useList[0]
    areaID = int(useList[1])
    towns = useList[2]

    print(townParser(towns,region,areaID))


