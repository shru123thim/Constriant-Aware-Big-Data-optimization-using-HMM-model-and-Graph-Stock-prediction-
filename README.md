# 🧠 CSP-Enhanced Financial Optimization System  
### Advanced Constraint-Aware Portfolio Management using Graphs, HMM, and CSP  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-blueviolet)
![HMM](https://img.shields.io/badge/Model-Hidden%20Markov%20Model-success)
![CSP](https://img.shields.io/badge/Optimization-Constraint%20Satisfaction%20Programming-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📘 Overview
**CSP-Enhanced Financial Optimization System** is a Python-based project that integrates  
📊 **Big Data Analytics**, 🕸️ **Graph Theory**, 🔮 **Hidden Markov Models (HMM)**, and 🧩 **Constraint Satisfaction Programming (CSP)**  
to perform **smart portfolio optimization** on real-world financial data from *Yahoo Finance (2018–2023)*.

It provides:
- Automated financial data loading and analysis  
- Hidden Markov Model-based market prediction  
- Constraint-aware investment strategy optimization  
- Interactive **Tkinter GUI** dashboard for users to visualize and manage results  

---

## ⚙️ Key Features
✅ **Automated dataset download** from Kaggle using `kagglehub`  
✅ **Graph-based investment modeling** using NetworkX  
✅ **HMM market prediction** via `hmmlearn`  
✅ **CSP optimization engine** with multiple constraints (risk, return, liquidity)  
✅ **Professional Tkinter GUI** with tabbed views for optimization, metrics, and documentation  
✅ **Performance metrics table** comparing CSP vs Standard optimization  

---

## 🗂️ Project Structure
📁 CSP-Financial-Optimization/
│
├── download_dataset.py # Downloads & converts Yahoo Finance dataset
├── main1.py # Performs base-level financial data analysis
├── main2.py # Runs constraint-aware financial optimization
├── gui_app.py # Tkinter-based CSP-enhanced GUI application
├── Yahoo_Finance_2018_2023.csv # Processed dataset
├── Yahoo_Finance_2018_2023.csv.xlsx # Original dataset
├── RUN.bat # Quick-run launcher
└── README.md # Project documentation

yaml
Copy code

---

## 🧩 System Workflow
Yahoo Finance Dataset (2018–2023)
↓
Data Preprocessing (pandas, numpy)
↓
Hidden Markov Model (hmmlearn)
↓
Graph Construction (networkx)
↓
Constraint Satisfaction Engine (python-constraint)
↓
Optimized Portfolio Recommendations
↓
Visualization & Controls via Tkinter GUI

yaml
Copy code

---

## 💡 Modules Explained

### 🗃️ 1. Dataset Download & Conversion (`download_dataset.py`)
- Downloads Yahoo Finance dataset using **KaggleHub**
- Converts `.xlsx` to `.csv` automatically
- Prints column names and data shape

### 📊 2. Data Analysis (`main1.py`)
- Loads CSV data  
- Performs statistical summaries  
- Displays column insights and numeric trends

### ⚡ 3. Constraint-Aware Optimization (`main2.py`)
- Builds **graph models** for strategies  
- Trains **HMM** for market states (Bearish, Neutral, Bullish)  
- Applies **constraints**:
  - Maximum portfolio risk  
  - Minimum portfolio return  
  - Liquidity mix  
- Generates **optimal investment paths**

### 🖥️ 4. CSP GUI Application (`gui_app.py`)
- Beautiful **blue-themed GUI** built with Tkinter and ttk  
- Tabs include:
  - **Main Optimization**
  - **CSP Solver**
  - **Performance Metrics**
  - **Technical Documentation**
- Supports data loading, constraint tuning, and real-time results display

---

## 📊 Performance Metrics

| Metric | Standard HMM | CSP-Optimized HMM | Graph + HMM | Graph + HMM + CSP | Improvement |
|--------|---------------|------------------|--------------|-------------------|-------------|
| Accuracy | 96.15% | 96.86% | 96.50% | 96.75% | +0.60% |
| Precision | 87.40% | 88.30% | 88.00% | 88.45% | +1.05% |
| Recall | 91.85% | 90.93% | 91.20% | 91.60% | −0.25% |
| F1-Score | 89.56% | 89.59% | 89.58% | 89.95% | +0.39% |
| MAPE | 3.85% | 3.14% | 3.50% | 3.25% | −0.60% |
| Execution Time | 2580s | 2520s | 100s | 110s | ⚡ 23.5× Faster |

---

## 🧮 Technologies Used

| Category | Libraries |
|-----------|------------|
| **Data Handling** | pandas, numpy |
| **Graph Modeling** | networkx |
| **Machine Learning** | hmmlearn |
| **Constraint Solver** | python-constraint |
| **GUI & Visualization** | tkinter, ttk, matplotlib |
| **Dataset Access** | kagglehub, openpyxl |

---

## 🚀 How to Run

### 🪟 **Windows (Quick Launch)**
Simply double-click:
```bash
RUN.bat
💻 Manual Setup
1️⃣ Install Required Packages
bash
Copy code
pip install pandas numpy networkx hmmlearn python-constraint kagglehub openpyxl matplotlib
2️⃣ Download Dataset
bash
Copy code
python download_dataset.py
3️⃣ Run Analysis
bash
Copy code
python main1.py
4️⃣ Execute Optimization
bash
Copy code
python main2.py
5️⃣ Launch GUI
bash
Copy code
python gui_app.py
📘 CSP Constraints Implemented
Portfolio Risk Constraint – Limits maximum allowed risk

Return Target Constraint – Enforces minimum return threshold

Strategy Count Constraint – Restricts max number of active strategies

Liquidity Mix Constraint – Maintains balance between liquid and illiquid assets

🎯 Results Summary
✅ Combined Graph + HMM + CSP for smart portfolio optimization
✅ Achieved 23.5× faster performance than traditional models
✅ Integrated constraint-based intelligence in portfolio selection
✅ Professional Tkinter GUI for ease of use and real-time analysis

👩‍💻 Author
👤 Mannava Shruthi
🎓 B.Tech – Computer Science & Engineering (Data Science)
💼 Project: Financial Optimization using CSP, HMM, and Graph Models



🏁 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute it for educational or research purposes.
