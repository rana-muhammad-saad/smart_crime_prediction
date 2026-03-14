import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load dataset (processed if cleaned, else raw)
df = pd.read_csv("C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/data/raw/smart_city_crime_dataset.csv", sep="\t")

# Features & target
X = df[["latitude", "longitude"]]  # can add more features later
y = df["arrest_made"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/models/crime_prediction_model.pkl")