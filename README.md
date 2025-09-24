# etl-sales-data
A collaborative project with AI (Chatgpt)

# ETL Sales Data Project

This project simulates a simple ETL (Extract, Transform, Load) pipeline for sales data.  

## Steps
1. **Extract** → Load raw sales data from `data/raw_sales.csv`
2. **Transform** → Clean missing values, standardize column names, and create derived fields
3. **Load** → Save the cleaned dataset into a new CSV file

## Tech Stack
- Python (pandas)
- CSV data source

## How to Run
```bash
python etl/etl_pipeline.py
