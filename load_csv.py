import pandas as pd


class LoadCsv:

    def __init__(self, origen_csv, node_csv, out_node_csv, temp_res_csv):
        self.origen_csv = origen_csv
        self.node_csv = node_csv
        self.out_node_csv = out_node_csv
        self.temp_res_csv = temp_res_csv

    def create_load_csv(self, input_csv, output_csv, node_id, node_label) -> None:
        df = pd.read_csv(input_csv)
        df = df[[node_id, node_label]]
        df.dropna(subset=[node_id, node_label], inplace=True)
        df.to_csv(output_csv, index=False)

    def create_nodes(self) -> None:
        self.create_load_csv(self.origen_csv, self.node_csv,'Id', 'Área de texto 1')
        return None

    def create_out_nodes(self) -> None:
        self.create_load_csv(
            self.origen_csv,
            self.out_node_csv,
            'Origem da linha',
            'Destino da linha'
        )
        return None

    def create_temp_res_nodes(self) -> None:
        self.create_load_csv(self.origen_csv, self.temp_res_csv, 'Id', 'r')
        return None
