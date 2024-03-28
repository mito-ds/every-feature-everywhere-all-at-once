# vanguard-fund-performance

#### Demo Overview
This demo shows how to use a variety of Mito's enterprise features to automate a standard report. Features include:
- CSV Imports
- Custom Imports (Enterprise)
- VLOOKUP 
- Custom Edits (Enterprise)
- Custom Sheet functions (Enterprise)
- Pivot Tables
- Conditional Formatting (Enterprise, only in Jupyter Demo)
- Export to Excel (only in Jupyter)

#### Scenario
You're a performance analyst at Vanguard. Your manager asked you to analyze the performance of each fund manager for each fund they are in charge of. 

### Streamlit Demo Instructions 

#### Launch the Streamlit app
This demo can be run with the `automation-app.py` Streamlit app. To launch the app, run the following commands:

```streamlit run automation-app.py```

#### Create automation
1. Import `fund_info.csv`
2. Use custom imports to import `fund performance` for 2022. Use a fake username and password.
3. Use Vlookup to add the Portfolio Manager from the fund_info dataframe into the performance dataframe
4. Notice that some of the funds have multiple portfolio managers. Use the `Separate Row On Delimiter` custom edit to split the portfolio managers into separate rows on the delimiter `, `.
5. Use the `GET_EMAIL` custom sheet function to get the email of each fund manager
6. Create a pivot table with the configuration below:
    - Rows: Fund Manager, email, Fund
    - Columns: Date (Grouped by Month)
    - Values: sum of MoM Return
7. Save the automation

#### Reuse automation
1. Click on the `Use Existing analysis` tab
2. Select the automation you just created
3. Upload the fund_info.csv file again 
4. Click `rerun`
5. Show the rebuilt analysis, voila! 

### Jupyter Demo Instructions 

#### Create automation
1. Import `fund_info.csv`
2. Use custom imports to import `fund performance` for 2022. Use a fake username and password.
3. Use Vlookup to add the Portfolio Manager from the fund_info dataframe into the performance dataframe
4. Notice that some of the funds have multiple portfolio managers. Use the `Separate Row On Delimiter` custom edit to split the portfolio managers into separate rows on the delimiter `, `.
5. Use the `GET_EMAIL` custom sheet function to get the email of each fund manager
6. Create a pivot table with the configuration below:
    - Rows: Fund Manager, Email, Fund
    - Columns: Date (Grouped by **Month**)
    - Values: sum of MoM Return
7. Add conditional formatting
    - less than 0, highlight in red
    - greater than 0, highlight in green
8. Generate code to create Excel file with formatting
9. Run code to generate Excel file
10. Open Excel file and show formatting

#### Reuse automation
1. Open the `change imported files` taskpane
    - Update the custom import conifguration to look at 2021
2. Rerun the analysis 
3. Show the updated Mitosheet 
4. Run the generated code
5. Show the new formatted Excel file, voila! 

### Dash Demo Instructions 

#### Launch the Streamlit app
This demo can be run with the `dash_app.py` Streamlit app. To launch the app, run the following commands:

```python -m dash_app.py```

#### Creation Automation
Instructions coming soon. Dash App already created.

