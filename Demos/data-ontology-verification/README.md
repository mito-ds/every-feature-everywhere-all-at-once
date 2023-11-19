# Data-ontology-verification

#### Demo Overview
This demo shows how Mito can be used to verify that data conforms to a required schema. This demo has two scenarios, one that uses Mito open source features and another that uses Mito enterprise features:

Mito open source features included in demo:
- Import csv files 
- Rename columns
- Convert data types
- IF statements
- column deleting
- VLOOKUP

Mito enterprise features included in demo:
- Custom edits 

#### Scenario
You work at a invoice processing company. Your company has an internal application that makes it easy for your customers to manage their invoices. However, the application requires that the data is in a specific format. Your job is to build Python scripts that ingest data from your customers, transform it into the data ontology required by your internal system, and then upload it to the application. 

# Demo Instructions

### Required Ontoogy
This is the ontology that your internal application requires:
- customer_name
- customer_email
- invoice_creation_date
- invoice_due_date
- total_amount
- is_open

### Jupyter Demo: Mito out of the box
- Import `tmobile_invoices.csv` and `tmobile_customer_info.csv`
- Rename `name_customer` to `customer_name` and `total_open_amount` to `total_amount`
- convert `invoice_creation_date` and `invoice_due_date` to datetimes 
- Create new column, `is_open` and calculate `IF(TYPE(clear_date) == 'NaN', 1, 0)`
- Delete `clear_date` 
- Use vlookup to get `customer_email` from based on `customer_name`

### Jupyter Demo: Mito Enterprise features
- Import verizon_invoices.xlsx
- Rename `email` to `customer_email`
- Delete unused columns: `customer_number`, `city`, `job`, `address`, `qty`
- Use a custom edit to make each row only contain one invoice instead of multiple
    - split the `total_amount`, `invoice_id`, `invoice_due_date`, and`invoice_creation_date`, `is_open` column on ` : ` separator
- Convert date columns to datetimes

### TODO: Create a streamlit app that guides the use through the demo



