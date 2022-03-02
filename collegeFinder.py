from flask import Flask, url_for, render_template, request
import math
from math import e

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

colleges = {
"Stanford" : 95,
"Yale": 93,
"UCLA": 93,
"MIT" : 91,
"Princeton": 97,
"Harvard": 95,
"Emory": 89,
"Berkely": 89
}

def get_gpa_index(GPA):
    if GPA == 5:
        return 0
    else:
        return (190*e**GPA)/(e**(2*GPA)+1)+5

def get_volunteer_index(hours):
    if hours <= 100:
        return .25*(-hours + 100)
    else:
        return -1*(hours-100)**(1/3)

def get_asb_index(asb):
    if asb == "Yes":
        return 0
    if asb == "No":
        return 15

def get_ap_index(p, t):
    diff = 5*(t - p)
    if t < 3:
        diff+=20
    elif t >= 3 and t < 6:
        diff+=10
    return diff

def college_index(gpa, pTaken, pPassed, vHours, ASB):
    return math.floor(100-get_gpa_index(gpa)-get_volunteer_index(vHours)-get_asb_index(ASB)-get_ap_index(pPassed, pTaken))

def get_colleges(cIndex):


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

    cinDex = college_index(gpa,pTaken, pPassed, vHours, ASB)
    get_colleges(cinDex)

    print("GPA Index = " + str(get_gpa_index(gpa)))
    print("Volunteer Index = " + str(get_volunteer_index(vHours)))
    print("ASB Index = " + str(get_asb_index(ASB)))
    print("AP Index = " + str(get_ap_index(pPassed, pTaken)))
    return render_template('results.html', index = cinDex)

if __name__=="__main__":
    app.run(debug=True)
