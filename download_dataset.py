# download_fixed.py
import kagglehub
import pandas as pd
import os

print("📥 Downloading Yahoo Finance Dataset...")

# Download the dataset
path = kagglehub.dataset_download("suruchiarora/yahoo-finance-dataset-2018-2023")

print(f"✅ Dataset downloaded to: {path}")

# List files
files = os.listdir(path)
print(f"📁 Files in dataset: {files}")

# Find the Excel file
excel_files = [f for f in files if f.endswith('.xlsx')]
if excel_files:
    excel_path = os.path.join(path, excel_files[0])
    print(f"📊 Excel file found: {excel_files[0]}")
    
    # Load Excel file with openpyxl engine
    try:
        df = pd.read_excel(excel_path, engine='openpyxl')
    except:
        # Try with xlrd as backup
        df = pd.read_excel(excel_path, engine='xlrd')
    
    print(f"📈 Data shape: {df.shape}")
    print(f"📋 Columns: {list(df.columns)}")
    print("\nFirst 3 rows:")
    print(df.head(3))
    
    # Save as CSV
    df.to_csv('Yahoo_Finance_2018_2023.csv', index=False)
    print("✅ Dataset saved as 'Yahoo_Finance_2018_2023.csv'")
else:
    print("❌ No Excel file found")