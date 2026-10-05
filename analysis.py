import pandas as pd

# Load the air quality dataset
df = pd.read_csv("data/city_day.csv")

# Display first 5 rows
print(df.head())
# Check dataset information
print("\nDataset Information:")
print(df.info())

# Check number of rows and columns
print("\nDataset Shape:")
print(df.shape)
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Check AQI statistics
print("\nAQI Statistics:")
print(df["AQI"].describe())
# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Check the data type of Date
print("\nDate Data Type:")
print(df["Date"].dtype)
# Check the date range
print("\nDate Range:")
print("Start Date:", df["Date"].min())
print("End Date:", df["Date"].max())
# Remove rows where AQI is missing
df = df.dropna(subset=["AQI"])

# Check the new dataset size
print("\nDataset shape after removing missing AQI:")
print(df.shape)

# Check remaining missing AQI values
print("\nMissing AQI values:")
print(df["AQI"].isnull().sum())
# Check missing-value percentage
print("\nMissing Value Percentage:")
missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent.sort_values(ascending=False))
# Remove Xylene because it has too many missing values
df = df.drop(columns=["Xylene"])

# Check the new number of columns
print("\nDataset shape after removing Xylene:")
print(df.shape)
# Fill missing numerical values with the median
numeric_columns = df.select_dtypes(include=["float64"]).columns

for column in numeric_columns:
    if column != "AQI":
        df[column] = df[column].fillna(df[column].median())

# Check remaining missing values
print("\nRemaining Missing Values:")
print(df.isnull().sum())
# Check number of records for each city
print("\nRecords by City:")
print(df["City"].value_counts())
# ==========================================
# EDA - EXPLORATORY DATA ANALYSIS
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a folder for graphs
os.makedirs("plots", exist_ok=True)


# ------------------------------------------
# GRAPH 1: Number of records by city
# ------------------------------------------

plt.figure(figsize=(12, 7))

city_counts = df["City"].value_counts()

city_counts.plot(kind="bar")

plt.title("Number of Air Quality Records by City")
plt.xlabel("City")
plt.ylabel("Number of Records")
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("plots/city_records.png")
plt.show()


# ------------------------------------------
# GRAPH 2: AQI Distribution
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.hist(df["AQI"], bins=50)

plt.title("AQI Distribution")
plt.xlabel("AQI")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("plots/aqi_distribution.png")
plt.show()


# ------------------------------------------
# GRAPH 3: Average AQI by City
# ------------------------------------------

city_aqi = df.groupby("City")["AQI"].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 7))

city_aqi.plot(kind="bar")

plt.title("Average AQI by City")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("plots/average_aqi_city.png")
plt.show()


# ------------------------------------------
# GRAPH 4: AQI Trend Over Time
# ------------------------------------------

daily_aqi = df.groupby("Date")["AQI"].mean()

plt.figure(figsize=(14, 6))

plt.plot(daily_aqi.index, daily_aqi.values)

plt.title("AQI Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Average AQI")

plt.tight_layout()

plt.savefig("plots/aqi_trend.png")
plt.show()


# ------------------------------------------
# GRAPH 5: Correlation Heatmap
# ------------------------------------------

numeric_df = df.select_dtypes(include=["float64", "int64"])

plt.figure(figsize=(12, 9))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f"
)

plt.title("Correlation Between Air Quality Variables")

plt.tight_layout()

plt.savefig("plots/correlation_heatmap.png")
plt.show()


# ------------------------------------------
# GRAPH 6: PM2.5 vs AQI
# ------------------------------------------

plt.figure(figsize=(10, 6))

plt.scatter(
    df["PM2.5"],
    df["AQI"],
    alpha=0.3
)

plt.title("PM2.5 vs AQI")
plt.xlabel("PM2.5")
plt.ylabel("AQI")

plt.tight_layout()

plt.savefig("plots/pm25_vs_aqi.png")
plt.show()


print("\n================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("Graphs saved inside the plots folder.")
print("================================")