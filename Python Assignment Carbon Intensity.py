# Installation instructions
'''
To check if the Requests module is already installed, navigate to the Python Command Prompt and write:
python -m pip show requests.
To install the Requests module, use 'python -m pip install requests' in the Command Prompt.

Likewise for json and matplotlib, respectively:
'python -m pip install json'
'python -m pip install matplotlib'
'''

'''
Data used from 
Distribution Network Areas: Energy Solutions: Understanding PES Distributor Areas: https://www.energybrokers.co.uk/electricity/PES-Distributor-areas
Carbon Intensity: https://carbonintensity.org.uk/
'''
import requests #Module required for API requests
import json #Module required for parsing JSON from API call
import matplotlib #Module required for making graphs

#Finding which region the postcode belongs to
#Region to postcode mapping data from Energy Solutions website

regions = {
    'East England': {
        'areaID': 10,
        'disNetwork': 'Eastern Electric',
        'postcodes': {'AL': [[1, 10]], 'CB': [[1, 11]], 'CM': [[0, 24]], 'CO': [[1, 16]], 'E': [4], 'EN': [[1, 11]], 'HA': [[0, 9]], 'HP': [[1, 8]], 'IG': [10], 'IP': [[1, 33]], 'LU': [[1, 7]], 'MK': [[44, 45]], 'N': [9, [11]], 'NR': [[1, 35]], 'NW': [2, 4, 7], 'PE': [[30, 38]], 'RM': [[1, 18]], 'G': [[1, 19]], 'SS': [[11, 17]], 'WD': [[1, 7]]}
    }
    'London'

    }
}




# headers = {
#     'Accept': 'application/json'
# }
#
# r = requests.get('https://api.carbonintensity.org.uk/intensity/date', params={}, headers=headers)
#
# data = r.json()
#
# print(json.dumps(data, indent=4))

