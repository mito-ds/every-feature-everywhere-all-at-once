import pandas as pd

def get_performance_data(username: str, password: str, year: int): 
    """
    Get Vangaurd fund performance data for a given year.

    The data returned by this function is an edited version of this data: https://www.kaggle.com/datasets/callumrafter/vanguard-investor-fund-data?select=performance.csv
    """
    performance = pd.read_csv('Demos/vanguard-enterprise/performance.csv')
    
    # Changed Date to dtype datetime
    performance['Date'] = pd.to_datetime(performance['Date'], infer_datetime_format=True, errors='coerce')

    # Filtered Date
    performance = performance[(performance['Date'] >= pd.to_datetime(f'{year}-01-01')) & (performance['Date'] < pd.to_datetime(f'{year + 1}-01-01'))]
    
    performance = performance.reset_index(drop=True)

    return performance


