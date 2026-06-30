from flask import Flask,render_template
'''
it creates an instances of flask class 
which will be your WSGI application
'''

####WSGI application 
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html> <h1> hello this soham first code </h1> </html> "

@app.route("/index")
def index():
    return render_template('index.html') #render template is used to run html file  with flask/python directly 

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True) 