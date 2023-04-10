import os
import pandas as pd
import pytest
from load_csv import LoadCsv


@pytest.fixture(scope="module")
def csv_file():
    # create a temporary csv file for testing
    df = pd.DataFrame({
        "Id": [1, 2, 3],
        "Text Area 1": ["text 1", "text 2", "text 3"],
        "Line Source": [1, None, 3],
        "Line Destination": [2, 3, None]
    })
    file_path = "./data_temporary_nodes.csv"
    df.to_csv(file_path, index=False)
    yield file_path
    # delete the temporary file after the test is done
    os.remove(file_path)


def test_create_nodes(csv_file):
    # test the create_nodes() method
    lc = LoadCsv(csv_file)
    lc.create_nodes()
    df = pd.read_csv("nodes.csv")
    assert len(df) == 3  # only 3 rows should remain after removing NaN values
    assert set(df.columns) == set(["Id", "Text Area 1"])  # only selected columns should remain
    assert df["Id"].tolist() == [1, 2, 3]  # check if the correct rows are left after removing NaN values


def test_create_out_nodes(csv_file):
    # test the create_out_nodes() method
    lc = LoadCsv(csv_file)
    lc.create_out_nodes()
    df = pd.read_csv("out_nodes.csv")
    assert len(df) == 1  # only 2 rows should remain after removing NaN values
    assert set(df.columns) == set(["Line Source", "Line Destination"])  # only selected columns should remain
    assert df["Line Source"].tolist() == [1]  # check if the correct rows are left after removing NaN values
    assert df["Line Destination"].tolist() == [2]  # check if the correct rows are left after removing NaN values
