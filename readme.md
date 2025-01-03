# Werkstudent Python Task by JEELKUMAR LANGALIA
Tools used : Git, GitHUB, VS Code

## Overview
This project is part of the Werkstudent Python interview task. The goal is to process data from sample invoices by extracting specific details, generating an Excel file with two sheets, and creating a CSV file. Additionally, an executable file is provided to simplify the process.


## How It Works

### Data Extraction
The script extracts the following details from the sample invoices:
1. **Invoice 1**:
   - **Date**: `2024-03-01`
   - **Value**: `381.12 €`
2. **Invoice 2**:
   - **Date**: `2016-11-26`
   - **Value**: `USD $950.00`

### Excel File Creation
- **Sheet 1**: Contains columns:
  - File Name
  - Date
  - Value
- **Sheet 2**: A pivot table summarizing:
  - Total value by date and document name.

### CSV File Creation
The CSV file mirrors the data in **Sheet 1**, separated by semicolons (`;`).


## Running the Code

### Option 1: Using the Executable File
1. Place the following files in the same folder as `script.exe`:
   - `sample_invoice_1.pdf`
   - `sample_invoice_2.pdf`
2. Double-click `script.exe` to execute the program.
3. The output files will be generated in the same folder:
   - `invoices_summary.xlsx`
   - `invoices_summary.csv`

### Option 2: Running the Python Script
1. Install Python and required libraries:
   ```bash
   pip install pandas openpyxl PyPDF2
