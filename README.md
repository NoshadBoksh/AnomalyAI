# AnomalyAI

AnomalyAI is a machine learning app that detects unusual patterns in time series data. Users can upload a CSV file and receive an instant report that highlights values that stand out from expected trends. The project demonstrates data cleaning, feature engineering, model selection, and interactive visual insight using Python pandas scikit learn and Streamlit.

## Features

* Upload your own CSV file with date and sales columns  
* Automatic detection of unusual data points using IsolationForest  
* Interactive chart to view trends and flagged anomalies  
* Clean project structure that is easy to extend or present in interviews  

## Project Structure

* app.py  
  The main Streamlit application  
* src folder with model.py  
  Contains the anomaly detection logic  
* scripts folder with generate_example_data.py  
  Creates a sample dataset for testing  
* data folder  
  Contains example_sales.csv  
* requirements.txt  
  All Python packages needed to run the project  

## How to Run

* Install dependencies  
  pip install -r requirements.txt  
* Generate example data  
  python scripts generate_example_data.py  
* Start the Streamlit app  
  streamlit run app.py  
* Upload your CSV and explore anomaly insights  

## Future Ideas

* Add product wise or category wise anomaly detection  
* Add a simple report view with summary statistics  
* Add an alert level for severe anomalies  
