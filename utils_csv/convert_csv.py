import csv


class CSVConverter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self) -> None:
        with open(self.input_file, "r") as input_file:
            csv_reader = csv.reader(input_file)
            # skip the header row
            header_row = next(csv_reader)
            # read the rest of the data
            data = [row for row in csv_reader]

        # convert the float numbers to int
        data = [[int(float(cell)) for cell in row] for row in data]

        # open the output CSV file and write the new data
        with open(self.output_file, "w", newline="") as output_file:
            csv_writer = csv.writer(output_file)
            # write the header row
            csv_writer.writerow(header_row)
            # write the rest of the data
            csv_writer.writerows(data)
