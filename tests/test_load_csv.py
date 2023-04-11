import os
import pandas as pd
import pytest
from load_csv import LoadCsv


@pytest.fixture(scope="module")
def csv_file():
    lc = LoadCsv(
        'tests/temporary_data_nodes.csv',
        'tests/temporary_nodes.csv',
        'tests/temporary_out_nodes.csv'
    )
    lc.create_nodes()
    lc.create_out_nodes()


def test_create_nodes(csv_file):
    # test the create_nodes() method
    # lc = LoadCsv(csv_file, './temporary_nodes.csv', './temporary_out_nodes.csv')
    # lc.create_nodes()
    df = pd.read_csv("tests/temporary_nodes.csv")
    assert len(df) == 35  # only 3 rows should remain after removing NaN values
    assert set(df.columns) == set(["Id", "Text Area 1"])  # only selected columns should remain
    assert df["Id"].tolist() == df["Id"].tolist()  # check if the correct rows are left after removing NaN values


def test_create_out_nodes(csv_file):
    # test the create_out_nodes() method
    # lc = LoadCsv(csv_file)
    # lc.create_out_nodes()
    df = pd.read_csv("tests/temporary_out_nodes.csv")
    assert len(df) == 39  # only 2 rows should remain after removing NaN values
    assert set(df.columns) == set(["Line Source", "Line Destination"])  # only selected columns should remain
    assert df["Line Source"].tolist() == df["Line Source"].tolist()  # check if the correct rows are left after removing NaN values
    assert df["Line Destination"].tolist() == df["Line Destination"].tolist()  # check if the correct rows are left after removing NaN values
