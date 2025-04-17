# Author: Ashmitha Thavarasa
# Date: 2023-10-01
# Title:

import time
import dask.dataframe as dd
import pandas as pd
import matplotlib.pyplot as plt
from dask.distributed import Client
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load data
full_data = dd.read_csv("trips_full_data.csv")
trip_data = pd.read_csv("trips_by_distance.csv")  # For filtering

# Strip leading/trailing spaces from column names
full_data.columns = full_data.columns.str.strip()
trip_data.columns = trip_data.columns.str.strip()

# Question 1a: People Staying Home
avg_stay_home = full_data.groupby('Week of Date')['Population Staying at Home'].mean().compute()
avg_stay_home.plot(kind='bar', title="Avg Population Staying at Home per Week")
plt.xlabel("Week")
plt.ylabel("Avg People Staying at Home")
plt.tight_layout()
plt.show()

# Travel Distances
distance_cols = ['Trips 1-25 Miles', 'Trips 25-100 Miles', 'Trips 100-250 Miles', 'Trips 250-500 Miles', 'Trips 500+ Miles']
distance_stats = full_data.groupby('Week of Date')[distance_cols].mean().compute()
distance_stats.plot(kind='bar', stacked=True, figsize=(12, 6), title="Distance Traveled by Week")
plt.xlabel("Week")
plt.ylabel("Avg Trips")
plt.tight_layout()
plt.show()

# Question 1b: Filter by Trip Counts > 10 Million
trip_10_25 = trip_data[trip_data['Number of Trips 10-25'] > 10000000]
trip_50_100 = trip_data[trip_data['Number of Trips 50-100'] > 10000000]

plt.figure(figsize=(10, 5))
plt.scatter(trip_10_25['Date'], trip_10_25['Number of Trips 10-25'], label='Trips 10–25')
plt.scatter(trip_50_100['Date'], trip_50_100['Number of Trips 50-100'], label='Trips 50–100', color='orange')
plt.xlabel("Date")
plt.ylabel("Number of Trips")
plt.title("Dates with >10M Trips (10–25 vs 50–100)")
plt.legend()
plt.tight_layout()
plt.show()

# Question 1c: Parallel Processing Comparison
n_processors = [10, 20]
n_processors_time = {}

for proc in n_processors:
    client = Client(n_workers=proc)
    start_time = time.time()

    # Re-run basic tasks
    _ = full_data.groupby('Week of Date')['Population Staying at Home'].mean().compute()
    _ = full_data.groupby('Week of Date')[distance_cols].mean().compute()
    _ = trip_data[trip_data['Number of Trips 10-25'] > 10000000]
    _ = trip_data[trip_data['Number of Trips 50-100'] > 10000000]

    dask_time = time.time() - start_time
    n_processors_time[proc] = dask_time
    client.shutdown()

for proc, t in n_processors_time.items():
    print(f"{proc} processors took {t:.2f} seconds")

# Question 1d: Regression Modeling
week_32 = trip_data[trip_data['Week'] == 32]
X = week_32[['Trips 1-25 Miles']].values
y = week_32['Number of Trips 10-25'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"RMSE: {rmse:.2f}")

# Question 1e: Visualize Traveler Counts by Distance
distance_stats.mean().plot(kind='bar', title="Average Number of Travellers by Distance")
plt.xlabel("Distance Categories")
plt.ylabel("Average Number of Trips")
plt.tight_layout()
plt.show()
