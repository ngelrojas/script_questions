import pytest
from anytree import Node, RenderTree, AsciiStyle
from link_nodes import LinkNodes


@pytest.fixture
def nodes():
    # create some sample nodes
    node1 = Node("Node 1", id=1)
    node2 = Node("Node 2", id=2, parent=node1)
    node3 = Node("Node 3", id=3, parent=node1)
    node4 = Node("Node 4", id=4, parent=node2)
    return {1: node1, 2: node2, 3: node3, 4: node4}


def test_create_link_nodes(nodes):
    # create the LinkNodes object
    link_nodes = LinkNodes("../link_nodes.csv")

    # create the link nodes
    nodes = link_nodes.create_link_nodes(nodes)

    # check that the nodes are connected correctly
    assert nodes[1].parent is None
    assert nodes[2].parent == nodes[1]
    assert nodes[3].parent == nodes[1]
    assert nodes[4].parent == nodes[2]

    # display the nodes for visual inspection
    for pre, fill, node in RenderTree(nodes[1], style=AsciiStyle()):
        print("%s%s" % (pre, node.name))
