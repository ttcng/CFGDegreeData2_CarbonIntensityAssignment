"""
----------------------------------------------------
Data used from:
Distribution Network Areas: Energy Solutions: Understanding PES Distributor Areas: https://www.energybrokers.co.uk/electricity/PES-Distributor-areas
Carbon Intensity: https://carbonintensity.org.uk/

Using the Carbon Intensity API provided by National Grid ESO, in partnership with Environmental Defense Fund Europe, 
University of Oxford Department of Computer Science and WWF.

This API provides the history for each region in Great Britain. The user inputs a town of their choice, which is used to 
find the associated region and its carbon intensity across the period of a chosen day.
----------------------------------------------------
Installation Instructions
To check if the Requests module is already installed, navigate to the Python Command Prompt and write:
python -m pip show requests.
To install the Requests module, use 'python -m pip install requests' in the Command Prompt.

Likewise for json and matplotlib, respectively:
'python -m pip install json'
'python -m pip install matplotlib'
"""
import os  # Package for finding relative directory
import requests  # Module required for API requests
import matplotlib.pyplot as plt  # Module required for making graphs
import datetime

# Reading text files in to create dictionary of town vs region.
# Dictionary for corresponding area IDs (usedby electricity distributors) and region IDs (used by API)

correspondingID = {
    10: 10,  # area ID to region ID
    11: 9,
    12: 13,
    13: 6,
    14: 8,
    15: 4,
    16: 3,
    17: 1,
    18: 2,
    19: 14,
    20: 12,
    21: 7,
    22: 11,
    23: 5,
}

# Setting up dictionary for town to region
townsToRegion = {}

# Function for adding each town to the dictionary
def townParser(someString, regionID, region):
    asList = someString.split(", ")
    for town in asList:
        townsToRegion[town] = {"regionID": regionID, "regionName": region}


fileList = os.listdir("townsData")
for fileName in fileList:
    areaID = fileName[:2]
    region = fileName[3:-4]
    tempRegionID = correspondingID[int(areaID)]

    with open("townsData/{}".format(fileName)) as f:
        towns = f.readlines()[
            4
        ]  # Excluding first three lines as turns out we don't need those
        townParser(towns, tempRegionID, region)

# User input to get town and check in dictionary
townData = None  # Wasn't a global variable so can use here
while townData is None:
    userInput = input("Enter a valid town in Britain: ")
    choice = userInput.title()
    townData = townsToRegion.get(choice)

regionID = townData["regionID"]
print(f'Your town is in the {region}.')

# Choice for API calls
date = input(
    "Please choose a date in the format dd/mm/yyyy or type 'now' for today's forecast: "
)
if len(date) == 3:
    date1 = str(datetime.date.today())
else:
    date1 = date[-4:] + "-" + date[3:5] + "-" + date[:2]

date2 = date1[:-1] + str(int(date1[-1]) + 1)


# Calling the API to get the data points for every half hour
def callAPI(regionID, date1, date2):
    headers = {"Accept": "application/json"}

    r = requests.get(
        "https://api.carbonintensity.org.uk/regional/intensity/{}T00:01Z/{}T00:00Z/regionid/{}".format(
            date1, date2, regionID
        ),
        params={},
        headers=headers,
    )
    data = r.json()
    return data


# Calling API
data = callAPI(regionID, date1, date2)

# Getting total carbon intensity per half hour
info = data["data"]
dnoRegion = info["dnoregion"]
region = info["shortname"]
dataPoints = []
times = []
for halfHour in info["data"]:
    timePoint = halfHour["from"][-6:-1]  # Getting just the times for the date in question
    times.append(timePoint)
    intensity = halfHour["intensity"]["forecast"]
    dataPoints.append(intensity)

graphName = f"Carbon Intensity on {date1} for {region}"

# Writing to a file
with open("results.txt", "a") as f:
    f.write(
        f"\n\nResults for {choice} on {datetime.date.today()}\n"
        f"The town chosen was {choice}.\n"
        + f"This town is in {region}, which has the electricity provider, {dnoRegion}.\n\n"
        + f"{graphName}:\n\n"
        + "Time   |  Carbon Intensity (gCO2/kWh)\n"
        + "-------------------------------------\n"
    )

    for i in range(len(times)):
        f.write(f"{times[i]}  |               {dataPoints[i]}\n")

print("The results file has been updated.")

# Showing plot
x_axis = times
y_axis = dataPoints
plt.plot(x_axis, y_axis)
plt.title(graphName)
plt.xlabel("Time")
plt.ylabel("Carbon Intensity in gCO2/kWh")

plt.xticks(rotation=45, ha="right")

# Getting every other tickmark on the hours instead of every half hour
a = plt.gca()
ax = a.axes
ax.set_xticks(ax.get_xticks()[::2])

plt.show()
