# main1.py - Yahoo Finance Big Data Optimization
import pandas as pd
import numpy as np
import networkx as nx
from hmmlearn import hmm
import matplotlib.pyplot as plt
from datetime import datetime
import random

print("🚀 YAHOO FINANCE BIG DATA OPTIMIZATION")
print("======================================")

class FinanceDataOptimizer:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.data = None
        
    def load_yahoo_data(self, file_path):
        """Load your Yahoo Finance dataset"""
        print(f"📊 Loading dataset: {file_path}")
        
        # Load your CSV file
        self.data = pd.read_csv(file_path)
        
        print("✅ Dataset loaded successfully!")
        print(f"   Shape: {self.data.shape}")
        print(f"   Columns: {list(self.data.columns)}")
        print(f"   First few rows:")
        print(self.data.head(3))
        
        return self.data
    
    def analyze_finance_data(self):
        """Analyze the financial data"""
        if self.data is None:
            print("❌ No data loaded!")
            return
            
        print("\n📈 FINANCIAL DATA ANALYSIS:")
        print("==========================")
        
        # Basic info
        print(f"Dataset size: {self.data.shape}")
        
        # Numeric columns analysis
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        print(f"\nNumeric columns: {list(numeric_cols)}")
        
        for col in numeric_cols[:5]:
            if col in self.data.columns:
                print(f"  {col}: mean={self.data[col].mean():.2f}, std={self.data[col].std():.2f}")
    
    def run_analysis(self, file_path):
        """Run complete analysis"""
        print("Starting Yahoo Finance Analysis...")
        print("=" * 50)
        
        # 1. Load data
        self.load_yahoo_data(file_path)
        
        # 2. Analyze data
        self.analyze_finance_data()
        
        print("\n🎉 ANALYSIS COMPLETE!")
        print("Next: We'll add graph and HMM models")

def main():
    optimizer = FinanceDataOptimizer()
    
    # Use the exact filename
    file_path = "Yahoo_Finance_2018_2023.csv"
    
    try:
        optimizer.run_analysis(file_path)
    except FileNotFoundError:
        print(f"❌ FILE NOT FOUND: {file_path}")
        print("Please make sure the file is in the same folder as this script")

if __name__ == "__main__":
    main()