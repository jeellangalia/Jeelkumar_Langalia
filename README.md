# Werkstudent Python Task by Jeelkumar Langalia
# Tools used : 
[![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org) 
[![GIT](https://img.shields.io/badge/GIT-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GITHUB](https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![VISUAL STUDIO CODE](https://img.shields.io/badge/VISUAL_STUDIO_CODE-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/en-us/microsoft-365/excel)
[![ChatGPT](https://img.shields.io/badge/CHATGPT-00A67E?style=for-the-badge&logo=openai&logoColor=white)](https://chat.openai.com)


## Overview of Task
This project is part of an interview task for the Werkstudent Python position. The goal of this task is to:
1. Extract specific details (like dates and values) from sample invoices.
2. Generate two output files:
   - **Excel file** with detailed and summarized data.
   - **CSV file** with raw extracted data.
3. Provide an executable file so the program can be run easily without needing Python installed.

This program was designed to make processing invoice data simple and efficient.

---

## Features
- **Data Extraction**: Reads invoice PDFs and extracts important details like dates and amounts.
- **Excel File Creation**:
  - **Sheet 1**: Raw data extracted from invoices.
  - **Sheet 2**: A summary table showing total amounts grouped by date.
- **CSV File Creation**: Outputs raw data in a standard format for easy sharing.
- **Executable File**: Allows users to run the program without installing Python.

---

## How to Use This Program

### Option 1: Using the Executable File (For Non-Technical Users)
1. **Download the Executable File**: (The executable file is too large for GitHub. You can download it here)
   - [Download script.exe](https://drive.google.com/drive/folders/1DQlo_vadCjdLhMUCDnRx4fbEXMj_VRsO?usp=drive_link)

2. **Prepare the Files**:
   - Place the following files in the same folder as the downloaded `script.exe`:
     - `sample_invoice_1.pdf`
     - `sample_invoice_2.pdf`

3. **Run the Program**:
   - Double-click `script.exe`. It will automatically process the invoices and create two output files:
     - `invoices_summary.xlsx`: An Excel file with all the extracted data.
     - `invoices_summary.csv`: A CSV file with the raw data.

4. **View the Outputs**:
   - Open `invoices_summary.xlsx` to see:
     - **Sheet 1**: Contains the file name, date, and value extracted from the invoices.
     - **Sheet 2**: A summary table showing total values grouped by date.
   - Open `invoices_summary.csv` to view the raw data in a text format.

---

### Option 2: Running the Python Script 
1. **Install Python**:
   - Download and install Python from [python.org](https://python.org).

2. **Install Required Libraries**:
   - Open a terminal or command prompt and run:
     ```bash
     pip install pandas openpyxl PyPDF2
     ```

3. **Run the Script**:
   - Place the script (`script.py`) and the invoice files in the same folder.
   - Run the script using this command:
     ```bash
     python script.py
     ```

4. **Check the Output**:
   - The Excel and CSV files will be created in the same folder as the script.

---

## Outputs
1. **Excel File (`invoices_summary.xlsx`)**:
   - **Sheet 1**: Raw extracted data with the following columns:
     | File Name              | Date       | Value   |
     |------------------------|------------|---------|
     | sample_invoice_1.pdf   | 2024-03-01 | 381.12  |
     | sample_invoice_2.pdf   | 2016-11-26 | 950.00  |
   - **Sheet 2**: A pivot table summarizing the total value grouped by date.

2. **CSV File (`invoices_summary.csv`)**:
   - A simple text-based file with the same data as Sheet 1 of the Excel file, separated by semicolons (`;`).

---

## What I Learned
1. How to extract text from PDFs using Python.
2. Creating Excel files with multiple sheets using `pandas` and `openpyxl`.
3. Automating workflows to save time on repetitive tasks.
4. Packaging Python scripts into executable files with `PyInstaller`.

---

## Challenges and Solutions
1. **PDF Formatting Issues**:
   - Challenge: The structure of the PDFs was inconsistent, making it difficult to extract data.
   - Solution: I manually identified keywords to locate the required information.

2. **Executable File Size**:
   - Challenge: The `.exe` file generated was larger than GitHub’s upload limit.
   - Solution: The file was hosted externally and linked in this README.

---

## How to Get the Executable
The executable file (`script.exe`) is too large to upload directly to GitHub. You can download it here:  
[Download script.exe](https://drive.google.com/drive/folders/1DQlo_vadCjdLhMUCDnRx4fbEXMj_VRsO?usp=drive_link)

---

## Files Included
- **`script.py`**: The Python script for extracting and processing the invoice data.
- **`script.exe`**: The executable file for non-technical users.
- **`invoices_summary.xlsx`**: The Excel file created by the program.
- **`invoices_summary.csv`**: The CSV file created by the program.
- **`README.md`**: This documentation.

---

## Improvements for the Future
- Automate data extraction more effectively for varying PDF formats using advanced techniques (e.g., regular expressions).
- Add error handling to notify users if files are missing or data extraction fails.
- Optimize the size of the executable file.

---

## Contact Information
If you have any questions or feedback, feel free to contact me:  
- **Name**: Jeelkumar Nikunjbhai Langalia 
- **Email**: jeelsoni1011@gmail.com

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/jeelsoni)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeelsoni)
[![Gmail](https://img.shields.io/badge/GMAIL-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jeelsoni1011@gmail.com)
[![Outlook](https://img.shields.io/badge/OUTLOOK-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:langalia21627@hs-ansbach.de)



Thank you for reviewing my submission! :)
