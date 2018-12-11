from flask import Flask
from flask import jsonify
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

# add getFOO to url or else error returned

@app.route('/getFOO')
def getFOO():
    cursor.execute("SELECT * FROM FOO;") 
    results = cursor.fetchall()
    data= []
    for row in results:
        data.append([x for x in row])
    return jsonify(data)
                
if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
