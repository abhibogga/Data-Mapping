#Imports 
from matplotlib import pyplot as plt #Data mapping 

import requests #Data Gathering 

import random #Random 


dataURL= "https://raw.githubusercontent.com/sixhobbits/ritza/master/data/us-cities.txt" #Imports every US city and its coordinates

r = requests.get(dataURL) #Gather data from above dataset


with open("us-cities.txt", "w") as f: 
  f.write(r.text)


lats = []
lons = []
colors = []
state_color = {} #We use curly braces for dictionaires 




all_colors = ["b", "g", "r", "c", "m", "y", "k"]


with open("us-cities.txt") as f: 
  for i, line in enumerate(f):
    state, lat, lon = line.split() #Organizes our data mapping
    lats.append(float(lat))
    lons.append(float(lon))

    if state not in state_color:
      state_color[state] = random.choice(all_colors)
    colors.append(state_color[state])


plt.scatter(lons,lats, c = colors)
plt.show()
      

