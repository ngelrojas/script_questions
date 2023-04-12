import csv
from anytree import Node, RenderTree, AsciiStyle

#
#
# import csv
# from anytree import Node, RenderTree, AsciiStyle
class ParentNodes:

    def __init__(self, node_file, answers_file_csv):
        self.node_file = node_file
        self.answers_file_csv = answers_file_csv

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

    def add_answer_nodes(self, nodes):
        with open(self.answers_file_csv, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            # skip the header row
            next(csvreader)
            for row in csvreader:
                # get the ID of the parent node and the label of the answer
                parent_id = int(row[0])
                answer_label = "[R]: " + row[1]
                # create a new node for the answer
                answer_node = Node(answer_label, id=parent_id)
                # get the parent node from the dictionary
                parent_node = nodes.get(parent_id)
                if parent_node:
                    # add the answer node as a child of the parent node
                    answer_node.parent = parent_node
        return nodes

    def display_nodes(self, menus):
        for node in menus.values():
            for pre, fill, n in RenderTree(node, style=AsciiStyle()):
                print(f"({n.id}): {n.name}")
        return None
