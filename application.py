from flask import Flask, render_template, request
from flask import jsonify
import json
import pyodbc

app = Flask(__name__)

@app.route('/',)
def func():
    cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:tataatsu-server.database.windows.net,1433;Database=tataatsu-database;Uid=tataatsuadmin@tataatsu-server;Pwd=Database@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = cnxn.cursor()

    #res = cursor.execute("SELECT * FROM uni")
    #op = []
    #for row in res:
    #    op.append(list(row))
    return "hello"
    
  
 
   # return jsonify(op)

app.run()
