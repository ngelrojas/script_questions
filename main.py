from utils_csv.load_csv import LoadCsv
from utils_csv.convert_csv import CSVConverter

from builder_tree.parent_nodes import ParentNodes
from builder_tree.link_nodes import LinkNodes

from menus.menu import Menu

# load the CSV file
apex = LoadCsv("nodes_csv/data_nodes.csv")
apex.create_load_csv("nodes_csv/nodes.csv", "Id", "Área de texto 1")
apex.create_load_csv("nodes_csv/out_nodes.csv", "Origem da linha", "Destino da linha")
apex.create_load_csv("nodes_csv/temp_response.csv", "Id", "r")

# convert items in the CSV file
converter = CSVConverter("nodes_csv/out_nodes.csv", "nodes_csv/link_nodes.csv")
converter.convert()

# create nodes
main_apex = ParentNodes("nodes_csv/nodes.csv", "nodes_csv/temp_response.csv")
node_menu = main_apex.create_nodes()
main_apex.display_nodes(node_menu)
node_menu_resp = main_apex.add_answer_nodes(node_menu)

# linking nodes
child_nodes = LinkNodes("nodes_csv/link_nodes.csv")
nodes = child_nodes.create_link_nodes(node_menu_resp)


def main():
    try:
        menu_options = {
            "(E)": "Sair",
        }
        while True:
            for key in menu_options:
                print(f"{key}: {menu_options[key]}")
                print("\n")

            id_node = input("Ingrese o numero da pergunta ou ('E' para sair): ")
            if id_node.isdigit():
                id_node = int(id_node)
                root_node = nodes[id_node]
                Menu(root_node).print_menu()
            elif id_node.lower() == "e":
                print("saindo...bye!")
                exit()

    except KeyError:
        print("Error: Could not find root node")


if __name__ == "__main__":
    main()
