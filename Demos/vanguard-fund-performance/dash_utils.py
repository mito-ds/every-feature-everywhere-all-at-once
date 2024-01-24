import pandas as pd
from mitosheet.extensions.v1 import ColumnHeader

def get_performance_data(username: str, password: str, year: int): 
    """
    Get Vangaurd fund performance data for a given year.

    The data returned by this function is an edited version of this data: https://www.kaggle.com/datasets/callumrafter/vanguard-investor-fund-data?select=performance.csv
    """
    performance = pd.read_csv('./performance.csv')
    
    # Changed Date to dtype datetime
    performance['Date'] = pd.to_datetime(performance['Date'], infer_datetime_format=True, errors='coerce')

    # Filtered Date
    performance = performance[(performance['Date'] >= pd.to_datetime(f'{year}-01-01')) & (performance['Date'] < pd.to_datetime(f'{year + 1}-01-01'))]
    
    performance = performance.reset_index(drop=True)

    return performance


def GET_EMAIL(full_name: pd.Series):   
    """
    {
        "function": "GET_EMAIL",
        "description": "Given a name, returns their email.",
        "search_terms": ["my_function"],
        "examples": [
            "GET_EMAIL('John Smith')",
            "GET_EMAIL('FULL_NAME0')"
        ],
        "syntax": "GET_EMAIL(full_name)",
        "syntax_elements": [{
                "element": "full_name",
                "description": "The name to lookup"
            }
        ]
    }
    """
    full_name = full_name.str.replace(' ', '.') + '@vanguard.com'

    return full_name


def separate_row_on_delimiter(
        df: pd.DataFrame, 
        attribute: ColumnHeader, 
        delimiter: str
    ) -> pd.DataFrame:
    # Get dtypes of original df
    dtypes = df.dtypes

    new_df = pd.DataFrame(columns = df.columns)

    error_count = 0
    for index, row in df.iterrows():

        attribute_list = row[attribute].split(delimiter)
        
        # Filter out any empty entries
        attribute_list = list(filter(lambda x: x != "", attribute_list))

        for index, val in enumerate(attribute_list):
            
            new_row = row
            new_row[attribute] = attribute_list[index]
            new_df.loc[len(new_df)] = new_row

    # Convert dtypes back to original dtypes
    for col in new_df.columns:
        new_df[col] = new_df[col].astype(dtypes[col])
            
    return new_df