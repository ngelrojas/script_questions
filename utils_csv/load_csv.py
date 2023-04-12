import pandas as pd


class LoadCsv:
    def __init__(self, origen_csv):
        self.origen_csv = origen_csv

    def create_load_csv(self, output_csv, node_id, node_label) -> None:
        df = pd.read_csv(self.origen_csv)
        df = df[[node_id, node_label]]
        df.dropna(subset=[node_id, node_label], inplace=True)
        df.to_csv(output_csv, index=False)
        return None
