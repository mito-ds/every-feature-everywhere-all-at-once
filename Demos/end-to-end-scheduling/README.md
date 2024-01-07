# Scheduling Demo

#### Demo Overview
This demo shows how to use Mito's scheduling functionality. Because this demo is intended to demonstrate Mito's scheduling functionality, the rest of the Mito workflow is simple. 

- Import a CSV
- Create a pivot table
- Add conditional formatting to the pivot table
- Export as an XLSX
- Schedule the resulting report

#### Scenario
You're a performance analyst at Vanguard. Your manager asked you to create a formatted pivot table that has the average performance of each fund

### JupyterLab Demo Instructions 

### Set the Scheduling enviornmental variables

Follow the documentation [here](https://docs.trymito.io/how-to/scheduling-your-automation) to set the env variables necessary for scheduling to work.

If you're on the Mito team, you can use [this repo](https://github.com/mito-ds/mito-automations-test) to test against. 

### Launch a Jupyter Notebook

Then, launch a Jupyter notebook with `jupyter lab`.

#### Create automation
1. Import `performance.csv`
2. Turn `Date` to a Datetime
3. Create a pivot table with the configuration below:
    - Rows: Date (Grouped by Year-Month)
    - Values: mean of MoM Return
4. Add a conditional format to set < 0 to red, and > 0 to green
5. Export to save file when running code, and export the pivot table as an Excel
6. Click Schedule in the Code tab,
    - Fill in the Automation Name (NOTE: this must be unique, so Mito can generate a unique branch name)
    - Fill in the automation description
    - Select a schedule to rerun at
    - Click `Schedule on Github`
7. Open the link that appears to see the Github PR
8. Click on the files to show that they have been uploaded, highlighting:
    - The necessary data files have been uploaded
    - The script has been parameterized automatically
    - Timezones have been handled correctly
    - The correct package versions have been frozen
9. Click on the Github action that is running on that PR, and then click `Summary`, and scroll down to see the results. 
10. Downloading the results file will give you a formatted Excel.