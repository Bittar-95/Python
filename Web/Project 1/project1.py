import sqlite3
from flask import *
con = sqlite3.connect("employee.db")
print("Database Opened Successfully")

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")
@app.route("/savedetailes",methods=["POST","GET"])
def saveData():
    message="Hello "
    if (request.method == "POST"):
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            with sqlite3.connect("employee.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO Employees (name,email,address) VALUES (?,?,?) ",(name,email,address))
                con.commit()
                message="Employee Succssfully Add"
        except:
            con.rollback()
            message="We Can Not Add Employee to The List"
        finally:
            return render_template("success25.html" , msg = message)
            con.close()
            


@app.route("/deleteEmployee",methods=["POST"])
def delete():
    message=""
    if (request.method == "POST"):
         try:
             ID = request.form["employeeID"]
             with sqlite3.connect("employee.db") as con:
                 cur = con.cursor()
                 cur.execute("Delete From Employees where id = ?",(ID))
                 con.commit()
                 message = "Successfully Delete User"
         except:
             con.rollback()
             message = "We Can not Delete The User Right Now"
             
         finally:
            return render_template("success25.html" , msg = message)
            con.close()
            
             
    
    
    
@app.route("/view")
def view():
    con = sqlite3.connect("employee.db")
    con.row_factory  =sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)






@app.route("/deletePage")
def deletePage():
    return render_template("delete.html")

app.run(debug=True)