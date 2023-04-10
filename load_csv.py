import pandas as pd


class LoadCsv:

    def __init__(self, origen_csv):
        self.origen_csv = origen_csv

    def create_nodes(self) -> None:
        """
        - select only the desired columns
        - remove all data with NaN values in the "Id" and "Área de texto 1" columns
        - save the resulting DataFrame to a new CSV file
        # CHANGE HERE
        # df = df[['Id', 'Área de texto 1']]
        :return: None
        """
        df = pd.read_csv(self.origen_csv)
        df = df[['Id', 'Text Area 1']]
        df.dropna(subset=["Id", "Text Area 1"], inplace=True)
        df.to_csv('nodes.csv', index=False)
        return None

    def create_out_nodes(self) -> None:
        """
        - read the new CSV file and create a new CSV file called links_nodes
        - with only the desired columns, like origem da linha, destino da linha
        - remove all data with NaN values in the "Origem da linha" and "Destino da linha" columns
        - select only the desired columns
        # CHANGE HERE
        # df.dropna(subset=["Origem da linha", "Destino da linha"], inplace=True)
        # CHANGE HERE
        # df = df[['Origem da linha', 'Destino da linha']]
        :return: None
        """
        df = pd.read_csv(self.origen_csv)
        df.dropna(subset=["Line Source", "Line Destination"], inplace=True)
        df = df[["Line Source", "Line Destination"]]
        df.to_csv('out_nodes.csv', index=False)
        return None
