import random
import streamlit as st
import pandas as pd
from mitosheet.streamlit.v1 import spreadsheet
# Import your database library here, e.g., import pymysql

def PREDICT_ITEM_CATEGORY(s):
    """
    {
        "function": "PREDICT_ITEM_CATEGORY",
        "description": "Labels the item with the AI-generated product category.",
        "search_terms": ["PREDICT_ITEM_CATEGORY"],
        "examples": [
            "PREDICT_ITEM_CATEGORY('MUG')",
            "PREDICT_ITEM_CATEGORY('PEN')"
        ],
        "syntax": "PREDICT_ITEM_CATEGORY(item)",
        "syntax_elements": [{
                "element": "item",
                "description": "The item to predict the category of"
            }
        ]
    }
    """


    labels = [
        "Office",
        "Kitchen",
        "Stationery",
        "Travel",
        "Bathroom",
        "Gifts",
    ]


    return s.apply(lambda x: random.choice(labels))


# Set the page layout to wide
st.set_page_config(layout="wide")

st.title("Transaction Categorization Tool")

st.info("""This tool uses AI to categorize transactions based on item descriptions. Ensure that the AI labels are correct before uploading the final results to the database. 
        
The labels can be any one of the following categories:
- Office
- Kitchen
- Stationery
- Travel
- Bathroom
- Gifts
""")

# Initialize session state variables if they don't exist
if 'ai_labeling_done' not in st.session_state:
    st.session_state['ai_labeling_done'] = False

if 'upload_done' not in st.session_state:
    st.session_state['upload_done'] = False

# When the AI Labeling button is clicked, update the session state to True
if st.button("Run AI Labeling") or st.session_state['ai_labeling_done']:
    st.session_state['ai_labeling_done'] = True

    dfs, code = spreadsheet('Demos/final-mile-data-cleaning/transaction_data.csv', sheet_functions=[PREDICT_ITEM_CATEGORY])
    
    # Only allow the user to click "Upload" if AI Labeling has been done
    if not st.session_state['upload_done']:
        if st.button("Upload Final Results to Database"):
            st.success("Results uploaded successfully!")
            st.session_state['upload_done'] = True
