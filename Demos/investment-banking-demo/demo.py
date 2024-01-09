import pandas as pd
import streamlit as st

# Make the page wide
st.set_page_config(layout="wide")

import os
# TODO: Remove these lines and replace with your own Snowflake credentials
os.environ['SNOWFLAKE_ACCOUNT'] = ''
os.environ['SNOWFLAKE_USERNAME'] = ''
os.environ['SNOWFLAKE_PASSWORD'] = ''

from mitosheet.streamlit.v1 import spreadsheet

def largest_recent_acquisitions():
    """
    Imports the largest recent mergers/acquisitions, as returned by 
    https://intellizence.com/insights/merger-and-acquisition/largest-merger-acquisition-deals/
    Domain: M&A
    """
    import pandas as pd
    dfs = pd.read_html('https://intellizence.com/insights/merger-and-acquisition/largest-merger-acquisition-deals/')
    return dfs[0]

def deals_done_by_industry_sector(sector: str):
    """
    Imports M&A deals conducted by the bank in a specified industry sector.
    Domain: M&A
    """
    # Fake data tailored to the specified sector
    return pd.DataFrame({
        'Deal': ['Deal 1', 'Deal 2'],
        'Sector': [sector, sector],
        'Value (Million $)': [500, 300],
        'Year': [2022, 2023]
    })

def import_historical_MA_deals(year_or_decade: str):
    """
    Imports historical M&A deals data filtered by year or decade.
    Domain: M&A
    """
    # Fake data for a given year or decade
    return pd.DataFrame({
        'Deal': ['Historical Deal 1', 'Historical Deal 2'],
        'Value (Billion $)': [10, 5],
        'Year': [year_or_decade, year_or_decade]
    })

def current_stock_prices():
    """
    Imports current stock prices from major stock exchanges.
    Domain: Market Data
    """
    # Simulated stock price data
    return pd.DataFrame({
        'Company': ['Company X', 'Company Y', 'Company Z'],
        'Stock Price ($)': [150, 120, 200],
        'Exchange': ['NYSE', 'NASDAQ', 'NYSE']
    })

def historical_market_performance(ticker: str, time_period: str):
    """
    Imports historical market performance data over a specified time period.
    Domain: Market Data
    """
    # Fake data for the given time period
    return pd.DataFrame({
        'Index': ['S&P 500', 'NASDAQ'],
        'Performance (%)': [10, 15],
        'Time Period': [time_period, time_period]
    })

def sector_performance_analysis(sector: str):
    """
    Analyzes and imports data on sector-wise market performance.
    Domain: Market Data
    """
    # Fake sector performance data
    return pd.DataFrame({
        'Sector': [sector, sector],
        'Performance (%)': [8, 12],
        'Year': [2022, 2023]
    })

def current_interest_rates():
    """
    Imports current interest rates from central banks or financial markets.
    Domain: Rates Information
    """
    # Simulated interest rates
    return pd.DataFrame({
        'Region': ['US', 'EU', 'UK'],
        'Interest Rate (%)': [2.5, 1.0, 0.75]
    })

def historical_exchange_rates(currency_pair: str):
    """
    Imports historical exchange rates for specific currency pairs.
    Domain: Rates Information
    """
    # Fake exchange rate data for a currency pair
    return pd.DataFrame({
        'Currency Pair': [currency_pair, currency_pair],
        'Exchange Rate': [1.15, 1.20],
        'Date': ['2022-06-01', '2023-06-01']
    })

def bond_yields_by_rating(rating: str):
    """
    Imports bond yields categorized by credit rating.
    Domain: Rates Information
    """
    # Fake bond yield data based on credit rating
    return pd.DataFrame({
        'Rating': [rating, rating],
        'Yield (%)': [3.5, 4.0],
        'Date': ['2023-01-01', '2023-07-01']
    })

st.title('Investment Banking Demo: Finding Missed Deals')

st.markdown("""
- **Data discoverability:**
custom importers allow strats to expose searchable domain-relevant datasets directly inside a spreadsheet.

- **Point-and-click Importing:**
built in import from XSLX and snowflake, custom importers allow imports from webpages.

- **Spreadsheet-style Joins:**
bankers can use VLOOKUPs, pivot tables, and other spreadsheet capabilities they already know.

- **Auto-documentation and repeatability from Python:**
bankers can share code snippets, making coordination with bankers easier.
""")

dfs, code = spreadsheet(
    import_folder='data',
    importers=[largest_recent_acquisitions, deals_done_by_industry_sector, import_historical_MA_deals, current_stock_prices, historical_market_performance, sector_performance_analysis,  current_interest_rates, historical_exchange_rates, bond_yields_by_rating]
)

# Expandable section that holds the code
with st.expander('Documented Data Prep Process'):
    st.code(code)

if st.button("Send Documented Process to Strats Team"):
    st.success("Code and documentation has been delivered to strats team, documenting this process. An email will be sent confirming your new process within 48 hours.")