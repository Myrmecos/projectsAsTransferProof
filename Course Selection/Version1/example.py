import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial
import pandas as pd


class InteractiveGraph:
    def __init__(self, G, node_pressed=None, xydata=None):
        self.G = G
        self.node_pressed = node_pressed
        self.xydata = xydata

    def refresh(self, show=True):
        plt.clf()
        nx.draw_networkx_labels(self.G, pos = nx.get_node_attributes(self.G, 'pos'))
        nx.draw_networkx_edges(self.G, pos = nx.get_node_attributes(self.G, 'pos'), width=1.0, alpha=0.5)
        plt.axis('off')
        #plt.axis((-4, 4, -1, 3))
        fig.patch.set_facecolor('white')
        if show:
            plt.show()

    def on_press(self, event):
        if event.inaxes is not None and len(self.G.nodes()) > 0:
            nodelist, coords = zip(*nx.get_node_attributes(self.G, 'pos').items())
            kdtree = scipy.spatial.KDTree(coords)
            self.xydata = np.array([event.xdata, event.ydata])
            close_idx = kdtree.query_ball_point(self.xydata, np.sqrt(0.1))
            i = close_idx[0]
            self.node_pressed = nodelist[i]

    def on_motion(self, event):
        if event.inaxes is not None and self.node_pressed:
            new_xydata = np.array([event.xdata, event.ydata])
            self.xydata += new_xydata - self.xydata
            #print(d_xy, self.G.nodes[self.node_pressed])
            self.G.nodes[self.node_pressed]['pos'] = self.xydata
            self.refresh(show=False)
            event.canvas.draw()

    def on_release(self, event):
        self.node_pressed = None


class Course:
    def __init__(self, id, name, prereq):
        self.id = id
        self.name = name
        self.prereq = prereq

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
pos = nx.planar_layout(G)
print(pos)


nodes = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
edges = np.array([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G']])
#pos = np.array([[0, 0], [-2, 1], [2, 1], [-3, 2], [-1, 2], [1, 2], [3, 2]])

IG = InteractiveGraph(G) #>>>>> add this line in the next step

nx.set_node_attributes(G, pos, 'pos')

fig, ax = plt.subplots()
fig.canvas.mpl_connect('button_press_event', lambda event: IG.on_press(event))
fig.canvas.mpl_connect('motion_notify_event', lambda event: IG.on_motion(event))
fig.canvas.mpl_connect('button_release_event', lambda event: IG.on_release(event))
IG.refresh(G) # >>>>> replace it with IG.refresh() in the next step