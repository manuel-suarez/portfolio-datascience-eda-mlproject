# 🏡 Airbnb Listings – EDA & Price Prediction (TO BE FINISHED)

## 📖 Project Overview

This project performs end-to-end data analysis and modeling on Airbnb listings data.  
It focuses on predicting listing price and availability using attributes like location, room type, number of reviews, and more.

Main steps:
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Regression Modeling
- Model Evaluation & Visualization

## 📊 Dataset

- Source: [Inside Airbnb](http://insideairbnb.com/get-the-data.html)
- File: `listings.csv` (from CDMX, México)
- Size: ~50k (48,544) rows
- Target variable: `price`

## 🛠️ Tools & Stack

- `pandas`, `numpy`
- `matplotlib`, `seaborn`, `plotly`
- `scikit-learn`
- `jupyter`, `streamlit` (optional)

## 📂 Project Structure

- `/data/`: raw and cleaned data
- `/notebooks/`: EDA and analysis
- `/src/`: reusable Python scripts
- `/outputs/`: model metrics and plots

## 🚀 Run Instructions

```bash
# Install dependencies
pip install -r requirements.txt

# Run preprocessing
python src/data_preprocessing.py
# Run feature engineering
python src/feature_engineering.py

📈 Outputs

* Correlation matrix
* Feature importances
* Price prediction metrics (RMSE, MAE, R²)

📄 License

MIT License. Dataset © Inside Airbnb (public use).
