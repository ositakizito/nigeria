from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods= ['POST', 'GET'])
def  index():
    if request.method == 'POST':
              user = request.form['choice']
              return render_template('index.html', user = user)                   
    else:
             user = request.args.get('choice')
             return render_template("index.html", user= user)     
             
                       
@app.route('/about')
def about():
    return  render_template("about.html")
 
if __name__ == '__main__':
     app.run(host = 'localhost' , debug = False)