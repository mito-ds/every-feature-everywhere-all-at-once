import json
import streamlit as st
import pandas as pd 
from mitosheet.streamlit.v1 import spreadsheet, RunnableAnalysis
import os
from custom_edits import separate_row_on_delimiter

from custom_functions import CHECK, GET_EMAIL
from custom_importers import get_performance_data

# Set the streamlit page to wide so you can see the whole spreadsheet
st.set_page_config(layout="wide")


st.title("Automation Builder")
st.markdown("""Need to build a new data automation? This app makes it easy

If you've already created an automation for the report, select that provider from below and click run! 

Otherwise, click the `Start new automation` button below to create a new automation.
""")

create_tab, consume_tab = st.tabs(["Start New Automation", "Use Existing Automation"])

with create_tab:

    provider_name = st.text_input("Provider Name", value="")

    # Create an empty spreadsheet
    analysis: RunnableAnalysis = spreadsheet(
        import_folder='./data',
        return_type='analysis',
        sheet_functions=[CHECK, GET_EMAIL],
        importers=[get_performance_data],
        editors=[separate_row_on_delimiter]
    )

    if st.button("Save automation"):
        # When the user clicks the button, save the generated_code returned by the spreadsheet 
        # component to a .py file in the /scripts directory.
        file_path = os.path.join(os.getcwd(), 'scripts', provider_name + '.py')
        with open(file_path, 'w') as f:
            f.write(analysis.to_json())
            st.success(f"""
                Automation successfully saved as {provider_name} 
            """)
            with st.expander("View Generated Python Code", expanded=False):
                st.code(analysis.fully_parameterized_function)


with consume_tab:

    # Read the file names from the scripts folder
    file_names = os.listdir(os.path.join(os.getcwd(), 'scripts'))

    # Remove the .py from the end
    file_names = [file_name.split('.')[0] for file_name in file_names]

    # Create a dropdown to select the file name
    file_name = st.selectbox("Select an automation", file_names)

    if file_name is None:
        st.stop()

    path = os.path.join(os.getcwd(), 'scripts', file_name + '.py')
    # Read the contents of the path
    with open(path, 'r') as f:
        json_string = f.read()

    analysis = RunnableAnalysis.from_json(json_string)

    st.markdown("### Upload the new Data files")

    # Create an object to store the new values for the parameters
    updated_metadata = {}

    # Loop through the parameters in the analysis to display imports
    for param in analysis.get_param_metadata():
        new_param = None

        # For imports that are exports, display a text input
        if param['subtype'] in ['file_name_export_excel', 'file_name_export_csv']:
            new_param = st.text_input(param['original_value'], value=param['initial_value'])
            
        # For imports that are file imports, display a file uploader
        elif param['subtype'] in ['file_name_import_excel', 'file_name_import_csv']:
            new_param = st.file_uploader(f"Select a new file to replace: **{param['original_value'].split('/')[-1]}**")
        
        if new_param is not None:
            updated_metadata[param['name']] = new_param

    # Show a button to trigger re-running the analysis with the updated_metadata
    run = st.button('Run')
    if run:
        result = analysis.run(**updated_metadata)
        spreadsheet(
            *result,
            import_folder='./data',
            return_type='analysis',
            sheet_functions=[CHECK, GET_EMAIL],
            importers=[get_performance_data],
            editors=[separate_row_on_delimiter]
        )

    

