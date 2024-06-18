import copy

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import copy

class Course:
    def __init__(self, id, name, prereq):
        self.id = id
        self.name = name
        self.prereq = prereq

class Node:
    def __init__(self, id):
        self.this = id
        self.preq = []
        self.enab = [] #courses that take this course as pre-requisite

def processCourseList(filename):
    df = pd.read_excel(filename)
    courseLst = []
    for i in range(len(df["id"])):
        prereq = df["prereq"][i]
        if pd.isna(prereq):
            prereq = []
        else:
            prereq = prereq.split("/")
        courseLst.append(Course(df["id"][i], df["name"][i], prereq))
    return courseLst

'''df = pd.read_excel("courseList.xlsx")
courseLst = []
for i in range(len(df["id"])):
    prereq = df["prereq"][i]
    if pd.isna(prereq):
        prereq = []
    else:
        prereq = prereq.split("/")
    courseLst.append(Course(df["id"][i], prereq))'''

'''courseLst = processCourseList("courseList.xlsx")
print(courseLst[1].name)
print(courseLst[1].prereq)

name = [i.name for i in courseLst]
print(name)'''

def makeGraph(courseLst, label = "id"):
    G = nx.DiGraph()

    if label == "id":
        for i in courseLst:
            #G.add_node(i.id)
            for j in i.prereq:
                G.add_edge(j, i.id)
    elif label == "name":
        for i in courseLst:
            for j in i.prereq:
                G.add_edge(j, i.name)
    return G
courseLst = processCourseList("courseList.xlsx")
G = makeGraph(courseLst)
G1 = makeGraph(courseLst, "name")
def prepareGraph(G):
    #pos = nx.spring_layout(G)
    pos = nx.planar_layout(G)
    #pos = nx.shell_layout(G)
    #pos = nx.planar_layout(G)
    print(pos)
    nx.set_node_attributes(G, pos, 'pos')
    #pos = posShift(pos, 0, 0)
    nx.draw_networkx_edges(G, pos, width=3, edge_color = "red")
    nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=[i.id for i in courseLst], node_color = 'yellow')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

def posShift(pos, x, y):
    for i in pos:
        print(i, pos[i])
        pos[i][0] += x
        pos[i][1] += y
        print(i, pos[i])
        print("----")


prepareGraph(G)



plt.axis('off')
plt.show()