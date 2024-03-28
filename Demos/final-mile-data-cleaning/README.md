# Instructions for Use

### Setup
1. Download the data for the demo here: https://www.kaggle.com/datasets/vipin20/transaction-data?resource=download
2. Upload it to the path `Demos/final-mile-data-cleaning/transaction_data.csv`
3. Start the app: `streamlit run Demos/final-mile-data-cleaning/main.py`

### Demo Instructions

Then, in the app:
1. Click the import button
2. Add a new column called Product Category
3. Use the `PREDICT_PRODUCT_LABEL` function on the item name to "AI label" the dataset
4. Then, find one of them that is wrong (most of them will be) - and relabel it. 
5. Then, click the "upload to database" button