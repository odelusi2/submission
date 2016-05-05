from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('arsenalopinions.html')
   
@app.route('/wenger')
def wenger():
   return render_template('AboutArseneWenger.html')
   
@app.route('/squad')
def squad():
   return render_template('ArsenalSquad.html')
   
@app.route('/register')
def register():
   return render_template('register.html')

@app.route('/signup')
def signup():
   return render_template('sign.html')   

@app.route('/Emirates')
def emirates():
   return render_template('TheEmirates.html')  

@app.route('/twitter')
def twitters():
   return render_template('twitter.html')  
   
@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("databsae.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("databsae.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)
   
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)