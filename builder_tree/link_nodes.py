import csv


class LinkNodes:
    def __init__(self, link_node_file):
        self.link_node_file = link_node_file

    def create_link_nodes(self, nodes):
        # read the links from the CSV file and connect the nodes
        with open(self.link_node_file, "r") as csvfile:
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
        return nodes
