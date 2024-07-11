#task3
#need pip install pandas,networkx and matplotlib to run code
import pandas as pd
import matplotlib.pyplot as plt
import csv
from csv import writer
plt.rcParams["figure.figsize"] = (50,50)
import networkx as nx

database = pd.read_excel(r'London Underground data.xlsx', sheet_name='Sheet1')#import excel document
database.columns=["Line", "Current Station", "Next Station", "Journey Length"]
database2 = database.dropna(axis=0, subset=['Journey Length'])#removes parts of database that don't include a journey time

#creates variables for each characteristic of the excel table
line = database2["Line"]
current_station = database2["Current Station"]
next_station = database2["Next Station"]
journey_length = database2["Journey Length"]

#convert each column of data into a list
linelist=list(line)
CSlist=list(current_station)
NSlist=list(next_station)
JLlist=list(journey_length)

#Creates empty graphs for each line to add stations to
Bakerloograph={}
Centralgraph={}
Circlegraph={}
Districtgraph={}
H_Cgraph={}
Jubileegraph={}
Metrograph={}
Northerngraph={}
Picgraph={}
Victoriagraph={}
W_Cgraph={}

#Loop through each station on excel spreadsheet to form one graph per line
for i in range(len(linelist)):
    if linelist[i] == "Bakerloo":
        count = len(Bakerloograph)
        Bakerloograph[count] = {CSlist[i] : [NSlist[i],JLlist[i]]}
    elif linelist[i] == "Central":
        count = len(Centralgraph)
        Centralgraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Circle":
        count = len(Circlegraph)
        Circlegraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "District":
        count = len(Bakerloograph)
        Districtgraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Hammersmith & City":
        count = len(H_Cgraph)
        H_Cgraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Jubilee":
        count = len(Jubileegraph)
        Jubileegraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Metropolitan":
        count = len(Bakerloograph)
        Metrograph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Northern":
        count = len(Northerngraph)
        Northerngraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Piccadilly":
        count = len(Bakerloograph)
        Picgraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Victoria":
        count = len(Bakerloograph)
        Victoriagraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}
    elif linelist[i] == "Waterloo & City":
        count = len(W_Cgraph)
        W_Cgraph[count] = {CSlist[i]: [NSlist[i], JLlist[i]]}

#Makes individual graphs for each line
plt.figure
BGP = nx.Graph()#Bakerloo Line Graph
for i in range(0,24):
    BGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
CeGP = nx.Graph()#Central Line Graph
for i in range(24, 73):
    CeGP.add_edge(CSlist[i], NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
CiGP = nx.Graph()#Circle Line Graph
for i in range(73, 108):
    CiGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
DGP = nx.Graph()#District Line Graph
for i in range(108,167):
    DGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
H_CGP = nx.Graph()#Hammersmith & City Line Graph
for i in range(167, 195):
    H_CGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
JGP = nx.Graph()#Jubilee Line Graph
for i in range(195,221):
    JGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
MGP = nx.Graph()#Metropolitan Line Graph
for i in range(221,257):
    MGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
NGP = nx.Graph()#Northern Line Graph
for i in range(257,308):
    NGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
PGP = nx.Graph()#Piccadilly Line Graph
for i in range(308,361):
    PGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
VGP = nx.Graph()#Victoria Line Graph
for i in range(361,376):
    VGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

plt.figure
WCGP = nx.Graph()#Waterloo & City Line Graph
for i in range(376,377):
    WCGP.add_edge(CSlist[i],NSlist[i],weight=JLlist[i])
plt.close()

#combines all the individual line graphs together
graphs={BGP,CeGP,CiGP,DGP,H_CGP,JGP,MGP,NGP,PGP,VGP,WCGP}

plt.figure
fullmap = nx.Graph()
fullmap=nx.compose_all(graphs)
nx.draw(fullmap, with_labels=True)
plt.close()
option=input("Would you like to a)Plot a new route? or b)See your journey history?")
if option==("a"):
    startstation=input("Enter Starting station")
    destination=input("Enter Destination")
    if startstation not in fullmap or destination not in fullmap:
        print("One or both of these stations are misspelled or blank. Check your input")
    else:
        dijk=nx.dijkstra_path(fullmap, startstation,destination, weight='weight')#networkx function which finds best route to traverse a graph(dijkstra's algorithm)
        dijklength=nx.dijkstra_path_length(fullmap, startstation,destination, weight='weight')#networkx function which calculates the total weight of the route taken by dijkstra's algorithm in the graph
        print("The stations travelled through are", dijk, "The journey will take", dijklength, "minutes")
        journeyssummary=[startstation,destination,dijk,dijklength]
        with open('Journeys.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(journeyssummary)
            f_object.close()
else:
    with open('Journeys.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)
