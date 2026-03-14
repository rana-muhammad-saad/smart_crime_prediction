import pandas as pd

# Load cleaned dataset
df = pd.read_csv("C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/data/processed/cleaned_crime_data.csv")

# --- Basic Info ---
def dataset_info():
    print("Dataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nStatistical Summary:")
    print(df.describe())

# --- Value Counts ---
def top_crimes(n=10):
    return df["crime_type"].value_counts().head(n)

def top_areas(n=10):
    return df["area"].value_counts().head(n)

# --- Arrest Analysis ---
def arrest_stats():
    return df["arrest_made"].value_counts()

# --- Run EDA ---
if __name__ == "__main__":
    dataset_info()
    print("\nTop Crimes:")
    print(top_crimes())
    print("\nTop Areas:")
    print(top_areas())
    print("\nArrest Distribution:")
    print(arrest_stats())