import pandas as pd

# Load raw data
df = pd.read_csv("C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/data/raw/smart_city_crime_dataset.csv", sep="\t")

# Strip whitespaces
df.columns = df.columns.str.strip()

# Convert date column
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Fill missing values
df['weapon_used'] = df['weapon_used'].fillna("None")
df['arrest_made'] = df['arrest_made'].fillna(0)

# Save cleaned data
df.to_csv("C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/data/processed/cleaned_crime_data.csv", index=False)

print("Cleaned data saved.")