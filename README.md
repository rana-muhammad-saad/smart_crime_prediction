# Smart City Crime Prediction VIP

## Folders:
- data/raw: Original CSV
- data/processed: Cleaned CSV
- src: Scripts for cleaning, analysis, training
- models: Saved ML model
- notebooks: EDA and visualization
- dashboard: Streamlit app
- reports/figures: Saved charts

## How to Run
1. Install packages:
   python -m pip install -r requirements.txt
2. Train model:
   python src/model_training.py
3. Run dashboard:
   streamlit run dashboard/app.py