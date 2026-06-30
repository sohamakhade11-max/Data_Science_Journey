from flask import Flask,render_template,request
'''
it creates an instances of flask class 
which will be your WSGI application
'''

####WSGI application 
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html> <h1> hello this soham first code </h1> </html> "

@app.route("/index",methods=['GET'])##by default the method is get method 
def index():
    return render_template('index.html') #render template is used to run html file  with flask/python directly 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"hello {name}!"
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True) 

'''
GET is used to retrieve data from the server and sends data through the URL.

POST is used to send data to the server and sends data in the request body. 
It is commonly used for form submission, login, signup, file upload, and database insertion operations.
'''