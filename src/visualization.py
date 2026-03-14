import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/data/processed/cleaned_crime_data.csv")

# Folder to save figures
fig_folder = "../reports/figures"
os.makedirs(fig_folder, exist_ok=True)

# --- Top Crimes Plot ---
def plot_top_crimes(n=10):
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, y="crime_type", order=df['crime_type'].value_counts().head(n).index)
    plt.title("Top Crime Types")
    plt.tight_layout()
    plt.savefig(os.path.join(fig_folder, "top_crime_types.png"))
    plt.show()

# --- Crimes by Area Plot ---
def plot_crimes_by_area(n=10):
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, y="area", order=df['area'].value_counts().head(n).index)
    plt.title("Crimes by Area")
    plt.tight_layout()
    plt.savefig(os.path.join(fig_folder, "crimes_by_area.png"))
    plt.show()

# --- Arrest Distribution Plot ---
def plot_arrest_distribution():
    plt.figure(figsize=(6,4))
    sns.countplot(x="arrest_made", data=df)
    plt.title("Arrest Made Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(fig_folder, "arrest_distribution.png"))
    plt.show()

# --- Run all plots ---
if __name__ == "__main__":
    plot_top_crimes()
    plot_crimes_by_area()
    plot_arrest_distribution()