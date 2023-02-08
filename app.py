from flask import Flask,render_template,request,session,redirect,url_for
import pandas as pd
app = Flask(__name__)
app.secret_key='asdsdfsdfs13sdf_df%&'
@app.route('/home',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      
      user = request.form['username']
      password = request.form['password']
      if user=='vnkgkl@gmail.com' and password=='123':
            session['username']=request.form['username']
         # importing csv module
            return render_template('home.html',login=login)
               
               
      else:
         return "User is not registered"
   return render_template('login.html')
@app.route("/")
def login():
  print("i am inside the home")
  return render_template('login.html')
@app.route('/ho',methods = ['POST', 'GET'])
def ho():
   if request.method == 'POST':
            num = request.form['num']
            n=0
            
            import csv
            result=[]
            # csv file name
            #filename = "books.csv"

            df = pd.read_csv('books.csv')
            df.to_csv('books.csv', index=None)

            # reading csv file
            data = pd.read_csv('books.csv')
            print("type",type(data))
            print("length",len(data))
            if num!='' and int(num)>0:
               print("nm",num)
               n=int(num)
            elif n < 1 or n==0:
               n=len(data)
            else:
               n=len(data)
            print("n values",n)
            for i in range(n):
               result.append(data.iloc[i])
            df = pd.DataFrame(result)
   return render_template('home.html', tables=[df.to_html()], titles="sno",login=login)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))
@app.route('/')
def index():
    login=False
    if 'username' in session:
        login=True
    return render_template('login.html',login=login)
if __name__== "__main__":
  app.run(host="0.0.0.0", port=int("5000"), debug=True)
