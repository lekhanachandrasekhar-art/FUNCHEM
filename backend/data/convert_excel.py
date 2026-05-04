import pandas as pd

# 📄 Input Excel file
excel_file = "periodic_data.xlsx"   # change to your file name

# 📄 Output CSV file
csv_file = "periodic_data.csv"

# Read Excel
df = pd.read_excel(excel_file)

# Save as CSV
df.to_csv(csv_file, index=False, encoding="utf-8")

print("✅ Conversion complete!")