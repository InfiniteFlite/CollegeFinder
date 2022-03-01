from flask import Flask, url_for, render_template, request
import math

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def get_gpa_index(GPA):
    if GPA == 5:
        return 0
    else:
        index = 5/((GPA**2)+0.3)
        return index

def get_vonunteer_index(hours):
    index = .2*(-hours + 100)
    return index

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")
def render_form():
    return render_template('form.html')

@app.route("/results")
def render_results():
    gpa = float(request.args['uGPA'])
    pTaken = int(request.args['uAPTaken'])
    pPassed = int(request.args['uAPpassed'])
    vHours = int(request.args['uvHours'])
    ASB = request.args['ASB']

    collegeIndex = 100-((pTaken-pPassed)*6)-((8-pTaken)*2)-get_gpa_index(gpa)-get_vonunteer_index(vHours)

    return render_template('results.html', index = collegeIndex)

if __name__=="__main__":
    app.run(debug=True)
