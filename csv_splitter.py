import os
import csv

def ensure_csv_extension(filename):
    """
    Ensures the filename has a .csv extension.
    
    Arguments:
        `filename`: The input filename.
        
    Returns:
        Filename with .csv extension.
    """
    return filename if filename.endswith(".csv") else filename + ".csv"

def get_output_filename(base_filename, start_row, end_row, output_path):
    """
    Generates the output filename with row range.
    
    Arguments:
        `base_filename`: The base name of the file.
        `start_row`: The starting row number of the output file.
        `end_row`: The ending row number of the output file.
        `output_path`: The path to save the output file.
        
    Returns:
        The full path of the output file.
    """
    return os.path.join(output_path, f"{base_filename}_{start_row}-{end_row}.csv")

def write_rows_to_file(writer, rows):
    """
    Writes rows to the CSV file using the writer object.
    
    Arguments:
        `writer`: CSV writer object.
        `rows`: List of rows to write.
    """
    for row in rows:
        writer.writerow(row)

def split_rows(filename, delimiter=",", row_limit=1000, output_path="."):
    """
    Splits a CSV file into multiple files with a specified row limit.
    
    Arguments:
        `filename`:  The input file path.
        `row_limit`: The number of rows every file should have, 1000 by default.
        `output_path`: Destination path. Current directory by default.
    """
    filename = ensure_csv_extension(filename)
    base_filename = os.path.splitext(os.path.basename(filename))[0]

    with open(filename, "r", newline='') as filehandler:
        input_file = csv.reader(filehandler, delimiter=delimiter)
        headers = next(input_file)

        current_row = 1
        start_row = 1
        rows_to_write = [headers]
        
        for i, row in enumerate(input_file, start=1):
            if i > current_row * row_limit:
                end_row = start_row + row_limit - 1
                current_out_path = get_output_filename(base_filename, start_row, end_row, output_path)
                with open(current_out_path, "w", newline='') as outfile:
                    writer = csv.writer(outfile, delimiter=delimiter)
                    write_rows_to_file(writer, rows_to_write)
                
                current_row += 1
                start_row = (current_row - 1) * row_limit + 1
                rows_to_write = [headers]
            
            rows_to_write.append(row)
        
        # Write the last set of rows
        end_row = start_row + len(rows_to_write) - 2
        current_out_path = get_output_filename(base_filename, start_row, end_row, output_path)
        with open(current_out_path, "w", newline='') as outfile:
            writer = csv.writer(outfile, delimiter=delimiter)
            write_rows_to_file(writer, rows_to_write)

def main():
    file_name = input("Input File Name: ")
    num_of_rows = input("Number of Rows: ")
    destination = input("Destination Path: ")
    
    try:
        split_rows(
            str(file_name), row_limit=int(num_of_rows), output_path=str(destination)
        )
        print("Done, come back soon!!!")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError:
        print("Error: Please enter a valid number for the row limit.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
