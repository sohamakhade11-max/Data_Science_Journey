from flask import Flask,render_template,request,redirect,url_for
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




###jinja 2 template engine 
'''
{{}} expression to print output in html that is in result.html file
{%..% conditions ,for loops }
{#..#} this is for comments'''


@app.route('/success/<int:score>')##variable rule
def success(score):
    # return "the  marks you got is "+score
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',results=res)

##jinja template
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result1.html',results=score)

##redirect and url_for
@app.route('/submit',methods=['GET','POST'])
def submit():
    avg_score=0
    if request.method=='POST':
        sci=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        ds=float(request.form['datascience'])

        avg_score=(sci+maths+c+ds)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('success',score=avg_score))

if __name__=="__main__":
    app.run(debug=True) 

