import pytest
from anytree import RenderTree, AsciiStyle
from builder_tree.link_nodes import LinkNodes
from builder_tree.parent_nodes import ParentNodes


@pytest.fixture
def load_nodes():
    main_apex = ParentNodes("tests/temporary_nodes.csv", "tests/temporary_resp_nodes.csv")
    nodes = main_apex.create_nodes()
    return nodes


def test_create_link_nodes(load_nodes):
    # create the LinkNodes object
    child_nodes = LinkNodes("tests/temporary_link_nodes.csv")
    nodes = child_nodes.create_link_nodes(load_nodes)

    # check that the nodes are connected correctly
    assert nodes[1].parent is None

    # display the nodes for visual inspection
    for node in nodes.values():
        for pre, fill, n in RenderTree(node, style=AsciiStyle()):
            print("%s%s" % (pre, n.name))
