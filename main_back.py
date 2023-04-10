import pandas as pd
import csv
from anytree import Node, RenderTree
# remove all data no necessary, to create nodes
# read the CSV file into a DataFrame
df = pd.read_csv('data_nodes.csv')

# select only the desired columns
# df = df[['Id', 'Origem da linha', 'Destino da linha', 'Área de texto 1']]
df = df[['Id', 'Área de texto 1']]
# save the resulting DataFrame to a new CSV file
df.to_csv('nodes.csv', index=False)


# remove all data no necessary, to create nodes
# read the CSV file into a DataFrame
df = pd.read_csv('data_nodes.csv')
df.dropna(subset=["Origem da linha", "Destino da linha"], inplace=True)
# select only the desired columns
df = df[['Origem da linha', 'Destino da linha']]

# save the resulting DataFrame to a new CSV file
df.to_csv('nodes_origin_dest.csv', index=False)
## ====================================================================================================

# Load data from CSV file
data = pd.read_csv("nodes.csv")

# Drop rows with NaN values in the "Id" and "Área de texto 1" columns
data.dropna(subset=["Id", "Área de texto 1"], inplace=True)

# Create nodes from the "Id" and "Área de texto 1" columns
nodes = [{"id": row["Id"], "text": row["Área de texto 1"]} for index, row in data.iterrows()]

df = pd.DataFrame(nodes)
df.to_csv('nodes_new.csv', index=False)
# Print the resulting nodes
# print(nodes)

## ====================================================================================================


# Read data from CSV file

# Read data from CSV file
# with open('nodes_new.csv', mode='r') as file:
#     reader = csv.reader(file)
#     next(reader)  # Skip header row
#     data = {int(row[0]): row[1] for row in reader}

# # Create root node
root = Node("Decision Tree")

# # Create nodes from data
# nodes = {}
# for id, text in data.items():
#     nodes[id] = Node(text, parent=root)
    
# print(nodes)
#
with open('nodes_origin_dest.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    data_node = {int(row[0]): row[1] for row in reader}
print(data_node)
# nodes_od = {}
# for id, text, t in data_node.items():
#     if text:
#         nodes_od[id] = Node(text, parent=root)

# print(nodes_od)
# Set parent-child relationships
# for id, node in nodes.items():
#     parent_id = id // 10
#     if parent_id in nodes:
#         node.parent = nodes[parent_id]

# # Print decision tree
# for pre, fill, node in RenderTree(root):
#     print("%s%s" % (pre, node.name))






## ====================================================================================================
# # create nodes from Área de texto 1
# # Open the CSV file
# with open('nodes.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    
#     # Loop through each row in the CSV file
#     for row in csv_reader:
#         # Extract the 'Id' column value
#         if row['Área de texto 1']:
#             node_id = row['Id'] + ' - ' + row['Área de texto 1']
        
#         # Create node using the extracted 'Id' value
#         # For example, you can print the node ID here
#         print("Node ID:", node_id)

## ====================================================================================================
# # create nodes from Origem da linha and Destino da linha columns
# # read in the csv file
# df = pd.read_csv('nodes.csv')

# # create a dictionary to store the nodes and leaf nodes
# nodes_dict = {}

# for i, row in nodes:
#     pass    
    # # get the values for the current row
    # node_id = str(row['Id'])
    # # print('ID:', row['Área de texto 1'])
    # # origem_id = row['Destino da linha'] == row['Id'] if row['Área de texto 1'] else ""
    # origem_l = str(row['Origem da linha'] == row['Id']) if not pd.isnull(row['Origem da linha']) else ""
    # destino_l = str(row['Destino da linha']) if not pd.isnull(row['Destino da linha']) else ""
    
    # # create the node and leaf nodes
    # node = {
    #     "id": node_id,
    #     "origem": {
    #         "id": origem_l,
    #         "leaf": True,
    #         "data": str(row['Área de texto 1'])
    #     },
    #     "destino": {
    #         "id": destino_l,
    #         "leaf": True,
    #         "data": str(row['Área de texto 1'])
    #     }
    # }
    
    # # add the node to the dictionary
    # nodes_dict[node_id] = node

# # print the resulting dictionary
# print(nodes_dict)

# load csv file
# df = pd.read_csv('nodes.csv')

# # drop rows with empty cells in 'Origem da linha' and 'Destino da linha' columns
# df.dropna(subset=['Origem da linha', 'Destino da linha'], inplace=True)

# # keep only 'Id', 'Origem da linha' and 'Destino da linha' columns
# df = df[['Id', 'Origem da linha', 'Destino da linha']]

# # print resulting dataframe
# print(df)


# using this example: Id,Origem da linha,Destino da linha
# 1,,
# 2,,
# 3,,
# 4,,
# 5,,
# 6,,
# 7,,
# 8,,
# 9,2,3
# remove all data without value, just kip it the data with value, to create nodes