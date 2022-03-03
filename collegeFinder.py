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
"Berkely": 89,
"UCSD": 84,
"University of Virginia": 83,
"Georgia Tech": 80,
"UC Davis": 77,
"Tulane": 82,
"Gonzaga": 75,
"TCU": 70,
"Temple": 69,
"RIT": 70,
"Seton Hall": 67,
"George Mason": 64,
"University of Idaho": 61,
"University of New Mexico": 58,
"Pace": 54,
"Gannon": 51,
"Harding": 50,
"Montana State": 48,
"Florida Atlantic": 46,
"South Dakota State University": 42,
"Husson": 40,
"Kieser": 40,
"Oakland University": 37,
"Tennessee State": 36,
"University of Alaska": 35,
"University of Toledo": 34,
"Wingate University": 31,
"Brandman University": 30,
"Valdosta": 28,
"Western Kentucky University": 26,
"William Woods": 25,
"University of the Cumberlands": 23,
"Wichita State": 21,
"William Carey": 20,
"University of Southern Mississippi": 18,
"Jackson State": 16,
"Grand Canyon University": 15,
"Ferris State": 13,
"Lindenwood": 11,
"Missouri State": 10,
"Morgan State": 7,
"SBCC": 0
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
    print(p)
    diff = 5*(t - p)
    print(diff)
    if t < 3:
        diff+=20
    elif t >= 3 and t < 6:
        diff+=10
    return diff

def college_index(gpa, pTaken, pPassed, vHours, ASB):
    index = math.floor(100-get_gpa_index(gpa)-get_volunteer_index(vHours)-get_asb_index(ASB)-get_ap_index(pPassed, pTaken))
    if index > 100:
        index = 100
    elif index < 0:
        index = 0
    return index

def get_colleges(cIndex):
    collegesIn = []
    for item in colleges.values():
        if cIndex > item:
            collegesIn.push(colleges.keys(item))

    return collegesIn

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

    return render_template('results.html', index = cinDex, colleges = get_colleges(cinDex))

if __name__=="__main__":
    app.run(debug=True)
