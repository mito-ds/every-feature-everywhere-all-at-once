import mitosheet
import pandas as pd
from mitosheet.extensions.v1 import ColumnHeader

def separate_row_on_delimiter(
    df: pd.DataFrame, 
    attribute: ColumnHeader, 
    delimiter: str) -> pd.DataFrame:

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