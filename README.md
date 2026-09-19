# Olist E-Commerce ETL Pipeline

An automated, end-to-end data pipeline built in Python to extract, transform, and analyze Brazilian e-commerce data from Olist. 

## Project Architecture
This project transitions manual data scripting into a modular, scalable ETL system:
* **`data_ingestion.py` (Extract):** Loads raw CSV data dynamically.
* **`data_transformation.py` (Transform):** Cleans and merges 5 distinct datasets (Orders, Reviews, Items, Products, Translations) into a centralized master DataFrame.
* **`business_questions.py` (Analyze):** Houses the business logic and aggregations.
* **`visual_reporter.py` (Visualize):** Automatically generates and exports business insights as charts.
* **`main.py` (Orchestration):** The control script that runs the entire pipeline sequentially.

## Key Insights Generated
1. **Monthly Revenue Trend:** Tracks total order value over time.
2. **Top Categories:** Identifies the top 10 highest-grossing product categories.
3. **Delivery Impact:** Analyzes how shipping delays affect customer review scores.
4. **Freight Analysis:** Compares the cost of shipping against the actual product price.

## How to Run
1. Ensure your raw CSV files are placed in the `data/` folder.
2. Install the required dependencies: `pandas`, `matplotlib`, `seaborn`.
3. Run the orchestrator from the root directory:
   ```bash
   python src/main.py
