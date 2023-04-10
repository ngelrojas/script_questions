import csv
from anytree import Node, RenderTree, AsciiStyle


class ParentNodes:

    def __init__(self, node_file):
        self.node_file = node_file

    def create_nodes(self):
        with open(self.node_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            # skip the header row
            next(csvreader)
            # create a dictionary to store the nodes
            nodes = {}
            for row in csvreader:
                # create a new node with the ID and label from the CSV row
                node_id = int(row[0])
                node_label = row[1]
                node = Node(node_label, id=node_id)
                # add the node to the dictionary
                nodes[node_id] = node
        return nodes

    def display_nodes(self, menus):
        for node in menus.values():
            for pre, fill, n in RenderTree(node, style=AsciiStyle()):
                print(f"{n.id}-{n.name}")
        return None
