from flask import Flask
from flask import jsonify
from flask import request
import pyodbc

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

server = 'vminformdev01' 
database = 'GI_VS_SC_Test' 

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

# add getFOO to url to get all
# add getFOO?id=<id> to get one foo

@app.route('/getFOO')

def getFOO():
    if 'id' in request.args:
        id = request.args['id']
        cursor.execute("SELECT * FROM FOO WHERE fooKey =" + id)
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return jsonify(results)
    else:
        cursor.execute("SELECT * FROM FOO;") 
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return jsonify(results)



@app.route('/test/<name>')
def nameTest(name):
    return 'name %s' % name

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
