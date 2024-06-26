# CSV File Splitter

A Python script to split large CSV files into smaller files with a specified number of rows. This tool is useful for managing large datasets and breaking them into more manageable pieces.

## Features

- **Handles filenames with or without `.csv` extension**: Automatically appends `.csv` if missing.
- **Customizable row limit**: Specify the number of rows per split file.
- **Header inclusion**: Ensures headers are included in all split files.
- **Dynamic output naming**: Output files are named with the original row number range they contain, making it easy to track the data.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/sd416/csv-splitter.git
    cd csv-splitter
    ```

2. Run the script:
    ```bash
    python split_csv.py -f my_data.csv -n 100 -d /path/to/output
    ```

3. arguments:

- **-f FILENAME, --filename FILENAME**
  - Name of the input CSV file. The .csv extension is optional.
  
- **-n NUM_ROWS, --num_rows NUM_ROWS**
  - Number of rows to include in each split file.
  
- **-d DESTINATION, --destination DESTINATION**
  - Directory path where the split files will be saved. Defaults to the current directory.



## Example

```bash

    python split_csv.py -f my_data.csv -n 100 -d /path/to/output

```

The output files will be named:


```bash
test_1-100.csv
test_201-300.csv
.
.
.
.
test_501-1000.csv
```
...
