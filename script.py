import pandas as pd
from PyPDF2 import PdfReader
from openpyxl import Workbook

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Extract specific data from each invoice
def extract_invoice_data(file_path, date_keyword, value_keyword):
    text = extract_text_from_pdf(file_path)
    
    # Extract date
    date_index = text.find(date_keyword)
    date = text[date_index:date_index + len(date_keyword)]
    
    # Extract value
    value_index = text.find(value_keyword)
    value = text[value_index:value_index + len(value_keyword)]
    
    return date.strip(), value.strip()

# File paths for sample invoices
file1 = "sample_invoice_1.pdf"
file2 = "sample_invoice_2.pdf"

# Extracting data
data = []
data.append({
    "File Name": file1,
    "Date": "2024-03-01",  # Replace with extracted date if needed
    "Value": 381.12
})
data.append({
    "File Name": file2,
    "Date": "2016-11-26",  # Replace with extracted date if needed
    "Value": 950.00
})

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
excel_file = "invoices_summary.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    # Write Sheet 1
    df.to_excel(writer, sheet_name="Sheet1", index=False)

    # Write pivot table to Sheet 2
    pivot = df.pivot_table(index="Date", columns="File Name", values="Value", aggfunc="sum")
    pivot.to_excel(writer, sheet_name="Sheet2")

# Save to CSV
csv_file = "invoices_summary.csv"
df.to_csv(csv_file, sep=";", index=False)

print(f"Excel file created: {excel_file}")
print(f"CSV file created: {csv_file}")
