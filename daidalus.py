import os
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/export', methods=['GET'])
def export_data():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    url_file = os.path.join(SITE_ROOT,'resources', "egrid2016_data.xlsx" )
    url ="https://www.epa.gov/sites/production/files/2018-02/egrid2016_data.xlsx"
    df_gen16 = pd.read_excel(url_file,sheet_name='GEN16',header=1, usecols='B,C,L')

    #return  df_gen16.to_html();

    return df_gen16.nlargest(5,'GENNTAN',keep='all').to_html()

#        to_json(orient="records")
#        df_gen16.to_html()




@app.route('/export/state/<filter>', methods=['GET'])
def dataByState(filter):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    url_file = os.path.join(SITE_ROOT, 'resources', "egrid2016_data.xlsx")
    url ="https://www.epa.gov/sites/production/files/2018-02/egrid2016_data.xlsx"
    columnas = 'A,B' + ',' + filter
    df_st16 = pd.read_excel(url_file,sheet_name='ST16',header=1,usecols=columnas)
    return df_st16.to_html()
#return df_st16.to_json(orient="records")

#excel.make_response_from_array([[1, 2], [3, 4]], "xlsx",
#                                         file_name="../egrid2016_data")


if __name__ == '__main__':
    app.run(debug=True)