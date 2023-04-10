from load_csv import LoadCsv
from convert_csv import CSVConverter
from parent_nodes import ParentNodes
from link_nodes import LinkNodes
from menu import Menu

# load the CSV file
apex = LoadCsv('data_nodes.csv')
apex.create_nodes()
apex.create_out_nodes()

# convert items in the CSV file
converter = CSVConverter('out_nodes.csv', 'link_nodes.csv')
converter.convert()

# create the nodes
main_apex = ParentNodes('nodes.csv')
node_menu = main_apex.create_nodes()
main_apex.display_nodes(node_menu)

# linking nodes
child_nodes = LinkNodes('link_nodes.csv')
nodes = child_nodes.create_link_nodes(node_menu)


def main():
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
                Menu(root_node).print_menu()
            elif id_node.lower() == "e":
                print('saindo...bye!')
                exit()

    except KeyError:
        print("Error: Could not find root node")


if __name__ == '__main__':
    main()
