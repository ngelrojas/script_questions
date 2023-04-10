import csv
from contextlib import redirect_stdout

import io

from parent_nodes import ParentNodes
from anytree import Node, RenderTree, AsciiStyle


def test_create_nodes():
    # create a test node file
    input_data = [['1', 'Node 1'], ['2', 'Node 2']]
    node_file = 'test_nodes.csv'
    with open(node_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Line Source', 'Line Destination'])
        writer.writerows(input_data)

    # create a ParentNodes instance and call create_nodes method
    parent_nodes = ParentNodes(node_file)
    nodes = parent_nodes.create_nodes()

    # check that the nodes were created and added to the dictionary
    assert len(nodes) == 2
    assert nodes[1].name == 'Node 1'
    assert nodes[1].id == 1
    assert nodes[2].name == 'Node 2'
    assert nodes[2].id == 2


def test_display_nodes():
    # create test data
    node1 = Node('Node 1', id=1)
    node2 = Node('Node 2', id=2, parent=node1)
    node3 = Node('Node 3', id=3, parent=node2)
    menus = {1: node1}

    # create instance of ParentNodes class
    parent_nodes = ParentNodes(node_file='test.csv')

    # call display_nodes method and check output
    # with io.StringIO() as buffer, redirect_stdout(buffer):
    assert parent_nodes.display_nodes(menus) is None

