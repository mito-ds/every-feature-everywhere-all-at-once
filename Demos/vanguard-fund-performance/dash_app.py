from mitosheet.mito_dash.v1 import Spreadsheet, mito_callback, activate_mito
from dash import Dash, html, Input, Output
import pandas as pd
from dash_utils import get_performance_data, GET_EMAIL, separate_row_on_delimiter

app = Dash(__name__)
activate_mito(app)

fund_info = pd.read_csv('./fund_info.csv')

app.layout = html.Div([
    html.H1('Fund Performance Dashboard'),
    Spreadsheet(
        fund_info, 
        id={'type': 'spreadsheet', 'id': 'sheet'},
        importers=[get_performance_data],
        sheet_functions=[GET_EMAIL],
        editors=[separate_row_on_delimiter],
        code_options={
            'as_function': True, 
            'call_function': False, 
            'function_name': 'build_fund_performanance_report', 
            'function_params': {'fund_info': 'df1'},
            'import_custom_python_code': True, 
        },
    ),
    html.Div(id='output')
])

@mito_callback(
    Output('output', 'children'),
    Input({'type': 'spreadsheet', 'id': 'sheet'}, 'spreadsheet_result'),
)
def update_output(spreadsheet_result):
    return html.Div([
        html.H3('Generated Python Code'),
        html.Code(spreadsheet_result.code(), style={'white-space': 'pre'}),
    ])

if __name__ == '__main__':
    app.run_server(debug=True)