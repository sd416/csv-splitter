import os
import csv
import argparse

def ensure_csv_extension(filename):
    return filename if filename.endswith(".csv") else filename + ".csv"

def get_output_filename(base_filename, start_row, end_row, output_path):
    return os.path.join(output_path, f"{base_filename}_{start_row}-{end_row}.csv")

def write_rows_to_file(writer, rows):
    for row in rows:
        writer.writerow(row)

def split_rows(filename, delimiter=",", row_limit=1000, output_path="."):
    filename = ensure_csv_extension(filename)
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    created_files = []

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
                
                created_files.append(os.path.basename(current_out_path))
                
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
        
        created_files.append(os.path.basename(current_out_path))

    return created_files

def main():
    parser = argparse.ArgumentParser(description="Split a CSV file into multiple files.")
    parser.add_argument("-f", "--filename", required=True, help="Input CSV file name")
    parser.add_argument("-n", "--num_rows", type=int, required=True, help="Number of rows per output file")
    parser.add_argument("-d", "--destination", default=".", help="Destination path for output files")
    
    args = parser.parse_args()
    
    try:
        created_files = split_rows(
            str(args.filename), row_limit=args.num_rows, output_path=str(args.destination)
        )
        print("The following files were created:")
        for file in created_files:
            print(file)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError:
        print("Error: Please enter a valid number for the row limit.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()