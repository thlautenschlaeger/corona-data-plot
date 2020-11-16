import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Download from here: https://www.arcgis.com/home/item.html?id=f10774f1c63e40168479a1feb6c7ca74
rki = pd.read_csv("RKI_COVID19.csv")

# Group data by date
rki = rki.groupby("Meldedatum").sum()
num_cases = rki.AnzahlFall

# Select the data from the RKI numbers
last_n_days = 60
vals = num_cases.values[-last_n_days:]
dates = pd.to_datetime(num_cases[-last_n_days + 7:].index.values).values
labels = list(num_cases[-last_n_days:].index)

# Prepare data to compute 7 day ratio
days_before = vals[:-7]
days_ahead = vals[7:]
week_ratio = (days_ahead / days_before)

# Plot stuff
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(dates, week_ratio)
ax.set(xlabel="Date",
       ylabel="7 day ratio",
       title="Corona 7 days new infections ratio in Germany")

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)
plt.savefig("7days_ratio.png", format="png")
plt.show()
