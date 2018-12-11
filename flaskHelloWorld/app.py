from flask import Flask
from flask import jsonify
from flask import request
import pyodbc

app = Flask(__name__)

server = 'vminformdev01' 
database = 'GI_VS_SC_Test' 

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

# add getFOO to url to get all
# add getFOO?id=<id> to get one foo

@app.route('/getFOO')

def getFOO():
    if 'id' in request.args:
        cursor.execute("SELECT * FROM FOO WHERE fooKey =" + request.args['id'])
    else:
        cursor.execute("SELECT * FROM FOO;")
       
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return jsonify(results)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
