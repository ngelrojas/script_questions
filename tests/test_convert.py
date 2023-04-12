import csv
import os
from utils_csv.convert_csv import CSVConverter


def test_csv_converter(tmpdir):
    # create a test input CSV file
    input_data = [["Origem da linha", "Destino da linha"], ["4.0", "5.0"]]
    input_file = tmpdir.join("test_input.csv")
    with open(str(input_file), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(input_data)

    # create a CSVConverter instance and convert the input file
    output_file = tmpdir.join("test_output.csv")
    converter = CSVConverter(str(input_file), str(output_file))
    converter.convert()

    # check that the output CSV file was created and contains the expected data
    assert os.path.isfile(str(output_file))
    with open(str(output_file), "r", newline="") as f:
        reader = csv.reader(f)
        header_row = next(reader)
        assert header_row == ["Origem da linha", "Destino da linha"]
        data = [row for row in reader]
        assert data == [["4", "5"]]
