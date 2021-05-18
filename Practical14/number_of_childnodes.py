from xml.dom.minidom import parse
import xml.dom.minidom
import os

os.chdir("/Users/jiayifan/IBI1_2020-21/Practical14")

DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

class Node:
    def __init__(self, id, children = [], parents = []):
        self.id = id
        self.children = children
        self.parents = parents

node_dict = locals()
node_list = []
for term in terms:
    term_id = term.getElementsByTagNameNS(term.namespaceURI, 'id')[0].childNodes[0].data #str
    is_a_list = []
    for id in term.getElementsByTagNameNS(term.namespaceURI, 'is_a'):
        is_a_list.append(id.childNodes[0].data) # a list of parents of one term
    node_dict[''+term_id] = Node(term_id, [], is_a_list)
    node_list.append(node_dict[''+term_id])

for Node in node_list: # e.g. term id: 001
    for parent_id in Node.parents: # parent id: 002,003,004
        node_dict[''+parent_id].children.append(Node.id) # 002'child:001; 003's child: 001,...

global descendant
descendant = []

# eg. child of 002: 001, 005, 009
def descendant_finder(Node):
    for child in Node.children:
        if not child in descendant:
            descendant.append(child)
            descendant_finder(node_dict[''+child])

def ChildNodes_finder(str):
    list = []
    for i in terms:
        defstr = i.getElementsByTagName('defstr')[0].childNodes[0].data
        if str in defstr:
            term_id = i.getElementsByTagNameNS(i.namespaceURI, 'id')[0].childNodes[0].data
            list.append(term_id)
    for term_id in list:
        descendant_finder(node_dict[''+term_id])
    print('the number of childNodes associated with', str, 'is',len(descendant))

count = []
ChildNodes_finder('DNA')
count.append(len(descendant))
descendant = []
ChildNodes_finder('RNA')
count.append(len(descendant))
descendant = []
ChildNodes_finder('protein')
count.append(len(descendant))
descendant = []
ChildNodes_finder('carbohydrate')
count.append(len(descendant))

import matplotlib.pyplot as plt
labels = ['DNA', 'RNA', 'protein', 'carbohydrate']
sizes = count

label_with_data = []
group = ''
for i in range (0,4):
    group = labels[i] + ' ' + str(count[i])
    label_with_data.append(group)

cmap = plt.get_cmap("Pastel1")
colors = cmap([1, 2, 3, 4, 5])

fig, ax = plt.subplots()
ax.pie(sizes, labels=label_with_data, autopct='%1.1f%%', shadow=False, startangle=90,colors=colors)
# legend
for ax in [ax]:
    ax.legend(labels,
            title="Molecule",
            loc="center left",
            bbox_to_anchor=(1,0,0.5,1))
# set_title
    ax.set_title("ChildNodes of four molecules")

plt.show()
