# Investment Banking Demo

This is a demo for the context of investment banking data. 

## Key Highlights:
1. On investment banking data
2. Custom importer that reads from a website
3. Importer grouping for data discoverability

## The Demo

You are an investment banking analyst, and you're trying to find companies that you have connections with, your bank has not done a deal with recently, but that have done mergers in aquisitions. In other words, missed deals! 

To do so:
1. First, import the CSV RECENT_TRANSACTIONS.csv
2. Then, import from largest_recent_acquisitions custom importer
3. Then, import the CRM.xlsx
4. Then, merge the RECENT_TRANSACTIONS and largest_recent_acquisitions into the CRM using VLOOKUPs on company name.
5. Filter on these two new columns to find entiries that are NOT in recent transactions, and ARE in largest_recent_acquisitions
6. You have you dataset -- you're done.