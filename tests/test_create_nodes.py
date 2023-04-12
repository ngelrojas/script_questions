import csv

from builder_tree.parent_nodes import ParentNodes
from anytree import Node


def test_create_nodes():
    # create a test node file
    input_data = [["1", "Node 1"], ["2", "Node 2"]]
    node_file = "tests/test_nodes.csv"
    temp_resp = "tests/temporary_resp_nodes.csv"
    with open(node_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Origem da linha", "Destino da linha"])
        writer.writerows(input_data)

    # create a ParentNodes instance and call create_nodes method
    parent_nodes = ParentNodes(node_file, temp_resp)
    nodes = parent_nodes.create_nodes()
    parent_nodes.add_answer_nodes(nodes)

    # check that the nodes were created and added to the dictionary
    assert len(nodes) == 2
    assert nodes[1].name == "Node 1"
    assert nodes[1].id == 1
    assert nodes[2].name == "Node 2"
    assert nodes[2].id == 2


def test_display_nodes():
    # create test data
    node1 = Node("Node 1", id=1)
    node2 = Node("Node 2", id=2, parent=node1)
    Node("Node 3", id=3, parent=node2)
    menus = {1: node1}

    # create instance of ParentNodes class
    parent_nodes = ParentNodes("tests/temporary_nodes.csv", "tests/temporary_resp_nodes.csv")

    assert parent_nodes.display_nodes(menus) is None
