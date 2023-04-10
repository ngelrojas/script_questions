import pandas as pd
import csv
from anytree import Node, RenderTree, AsciiStyle

# 1 - read the CSV file  and create a new CSV called nodes file with only the desired columns,
# like id, area de texto 1
df = pd.read_csv('data_nodes.csv')

# select only the desired columns
df = df[['Id', 'Área de texto 1']]
# 1.1 remove all data with NaN values in the "Id" and "Área de texto 1" columns
df.dropna(subset=["Id", "Área de texto 1"], inplace=True)
# save the resulting DataFrame to a new CSV file
df.to_csv('nodes.csv', index=False)

# 2 - read the new CSV file and create a new CSV file called links_nodes
# with only the desired columns, like origem da linha, destino da linha
df = pd.read_csv('data_nodes.csv')
# 2.2 remove all data with NaN values in the "Origem da linha" and "Destino da linha" columns
df.dropna(subset=["Origem da linha", "Destino da linha"], inplace=True)
# select only the desired columns
df = df[['Origem da linha', 'Destino da linha']]
# save the resulting DataFrame to a new CSV file
df.to_csv('out_nodes.csv', index=False)

# convert float number in int number

with open('out_nodes.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    # skip the header row
    header_row = next(csv_reader)
    # read the rest of the data
    data = [row for row in csv_reader]

# convert the float numbers to int
data = [[int(float(cell)) for cell in row] for row in data]

# open the output CSV file and write the new data
with open('link_nodes.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    # write the header row
    csv_writer.writerow(header_row)
    # write the rest of the data
    csv_writer.writerows(data)

# create nodes
# open the CSV file and read the data into a list
with open('nodes.csv', 'r') as csvfile:
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

# open the CSV file with the links and create the connections
with open('link_nodes.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # skip the header row
    next(csvreader)
    for row in csvreader:
        # get the IDs of the source and target nodes
        source_id = int(row[1])
        target_id = int(row[0])
        # create the connection between the nodes
        if source_id == target_id:
            target_node = None
        else:
            target_node = nodes[target_id]
        nodes[source_id].parent = target_node

# print the tree for testing purposes
# for pre, fill, node in RenderTree(nodes[14], style=AsciiStyle()):
#     print(f"{pre}{node.name}")
for node in nodes.values():
    for pre, fill, n in RenderTree(node, style=AsciiStyle()):
        print(f"{pre}{n.id}-{n.name}")

























