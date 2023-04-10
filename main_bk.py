import pandas as pd
import csv
from anytree import Node, RenderTree, AsciiStyle


# 1 - read the CSV file  and create a new CSV called nodes file with only the desired columns,
# like id, area de texto 1
df = pd.read_csv('data_nodes.csv')
# select only the desired columns
# CHANGE HERE
# df = df[['Id', 'Área de texto 1']]
df = df[['Id', 'Text Area 1']]
# 1.1 remove all data with NaN values in the "Id" and "Área de texto 1" columns
df.dropna(subset=["Id", "Text Area 1"], inplace=True)
# save the resulting DataFrame to a new CSV file
df.to_csv('nodes.csv', index=False)

# 2 - read the new CSV file and create a new CSV file called links_nodes
# with only the desired columns, like origem da linha, destino da linha
df = pd.read_csv('data_nodes.csv')
# 2.2 remove all data with NaN values in the "Origem da linha" and "Destino da linha" columns
# CHANGE HERE
# df.dropna(subset=["Origem da linha", "Destino da linha"], inplace=True)
df.dropna(subset=["Line Source", "Line Destination"], inplace=True)
# select only the desired columns
# CHANGE HERE
# df = df[['Origem da linha', 'Destino da linha']]
df = df[["Line Source", "Line Destination"]]
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

menus = {}
# read the nodes from the CSV file and create the tree
with open('nodes.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # skip the header row
    next(csvreader)
    # create a dictionary to store the nodes
    nodes = {}
    menu = {}
    for row in csvreader:
        # create a new node with the ID and label from the CSV row
        node_id = int(row[0])
        node_label = row[1]
        node = Node(node_label, id=node_id)
        # add the node to the dictionary
        nodes[node_id] = node
        menus[node_id] = node

for node in menus.values():
    for pre, fill, n in RenderTree(node, style=AsciiStyle()):
        print(f"{n.id}-{n.name}")


# read the links from the CSV file and connect the nodes
with open('link_nodes.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # skip the header row
    next(csvreader)
    for row in csvreader:
        # get the IDs of the source and target nodes
        source_id = int(row[0])
        target_id = int(row[1])
        # create the connection between the nodes
        if source_id == target_id:
            target_node = None
        else:
            target_node = nodes[source_id]
        nodes[target_id].parent = target_node


# function to recursively print the menu for a given node

def print_menu(node, indent=""):
    # print the node label and ID
    print(f"{indent}{node.id}: {node.name}")
    # recursively print the menu for each child node
    children = node.children
    if not children:
        return
    for child in children:
        print(f"\t({child.id}):{child.name} ")
    choice = input("Selecione a seguiente opcao ou ('b' para voltar e 'e' pasa sair ): ")
    if choice == 'b':
        return
    elif choice == 'e':
        print('saindo...')
        exit()
    selected_node = None
    for child in children:
        if str(child.id) == choice:
            selected_node = child
            break
    if not selected_node:
        print("Invalid choice. Please try again.")
        print_menu(node)
    else:
        print_menu(selected_node)


# print the entire menu starting from the root node
try:
    menu_options = {
        "E": "Sair",
    }
    while True:
        for key in menu_options:
            print(f"{key}: {menu_options[key]}")

        id_node = input("Ingrese o numero da pergunta ou ('E' para sair): ")
        if id_node.isdigit():
            id_node = int(id_node)
            root_node = nodes[id_node]
            print_menu(root_node)
        elif id_node == "e":
            print('saindo...')
            exit()

except KeyError:
    print("Error: Could not find root node")
