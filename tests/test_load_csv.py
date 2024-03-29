import pandas as pd
import pytest
from utils_csv.load_csv import LoadCsv


@pytest.fixture(scope="module")
def csv_file():
    lc = LoadCsv("tests/temporary_data_nodes.csv")
    lc.create_load_csv("tests/temporary_nodes.csv", "Id", "Área de texto 1")
    lc.create_load_csv("tests/temporary_out_nodes.csv", "Origem da linha", "Destino da linha")
    lc.create_load_csv("tests/temporary_resp_nodes.csv", "Id", "r")


def test_create_nodes(csv_file):
    # test the create_nodes() method
    df = pd.read_csv("tests/temporary_nodes.csv")
    assert len(df) == 35
    assert set(df.columns) == set(["Id", "Área de texto 1"])
    assert df["Id"].tolist() == df["Id"].tolist()


def test_create_out_nodes(csv_file):
    df = pd.read_csv("tests/temporary_out_nodes.csv")
    assert len(df) == 39  # only 2 rows should remain after removing NaN values
    assert set(df.columns) == set(["Origem da linha", "Destino da linha"])
    assert df["Origem da linha"].tolist() == df["Origem da linha"].tolist()
    assert df["Destino da linha"].tolist() == df["Destino da linha"].tolist()


def test_create_resp_nodes(csv_file):
    df = pd.read_csv("tests/temporary_resp_nodes.csv")
    assert len(df) == 27  # only 2 rows should remain after removing NaN values
    assert set(df.columns) == set(["Id", "r"])
    assert df["Id"].tolist() == df["Id"].tolist()
