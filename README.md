# Mobility Analysis with Big Data and Parallel Processing

## 📊 Overview
This project investigates how big data and parallel computing can be used to improve the processing time and efficiency of mobility analysis by the Bureau of Transportation Statistics (BTS). The analysis is based on anonymized mobile device location data and focuses on how far people travel, how many stay at home, and how frequently trips are taken.

---

## 📁 Datasets Used

- `trips_by_distance.csv`: Contains number of trips per day categorized by trip frequency.
- `trips_full_data.csv`: Contains weekly mobility statistics including distances traveled and people staying home.

---

## ⚙️ Project Objectives

- 🏠 **Quantify how many people stay at home per week**
- 🚗 **Determine how far people travel when they leave home**
- 📅 **Compare days with >10 million trips in 10–25 vs 50–100 range**
- 🧠 **Use regression models to simulate trip frequency based on distance**
- 🧮 **Compare processing times using 10 vs 20 processors with Dask**
- 📊 **Visualize behavior patterns for policy-making and urban planning**

---

## 🚀 Technologies

- Python 3.x
- Dask (for parallel processing)
- Pandas (for serial data manipulation)
- scikit-learn (for regression modeling)
- matplotlib (for visualizations)

---

## 🧪 How to Run

```bash
# Create environment
pip install -r requirements.txt

# Start Dask dashboard 
dask-scheduler
dask-worker localhost:8786

# Run the analysis
python project.py
