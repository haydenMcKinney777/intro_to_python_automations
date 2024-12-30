"""

docs: https://tedboy.github.io/flask/generated/generated/flask.Request.html
"""

from flask import Flask, render_template, request

app = Flask(__name__)                                      #initialize flask

@app.route('/')                                            #when the user visits the homepage, we want function home() to run. this is a standard GET request
def home():
    print("GET request")
    return render_template('index.html')                   #flask will go into our 'templates' folder, and render index.html. This is why a templates folder is always required.

@app.route('/', methods = ['POST'])                        #here we are allowing our flask app to be able to handle POST requests, which we will need for when the user sends the data for the volume to be computed.                   
def home_post():
    dim1 = request.form.get('first_dimension')
    dim2 = request.form.get('second_dimension')
    dim3 = request.form.get('third_dimension')
    volume = float(dim1) * float(dim2) * float(dim3)
    print("POST request")
    return render_template('index.html', output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)    #renders the html page again but passes the calculated volume as a variable 'output' so that it can be displayed on the page. we also send dim1, dim2, dim3 again so that when we calculate the output, the parameters that the user entered do not disappear.
app.run()                                                  #run our app on localhost
