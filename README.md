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
    python csv_splitter.py
    ```

3. Follow the prompts:
    - **Input File Name**: Name of the input CSV file (with or without `.csv` extension).
    - **Number of Rows**: Number of rows per split file.
    - **Destination Path**: Directory where the split files will be saved.

## Example

```bash
Input File Name: test
Number of Rows: 500
Destination Path: /path/to/output

```

The output files will be named:

test_1-500.csv

test_501-1000.csv

...
